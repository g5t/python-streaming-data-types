from dataclasses import dataclass
from datetime import datetime, timezone
from typing import NamedTuple

import flatbuffers
import numpy

import streaming_data_types.fbschemas.histogram_hm00.Attribute as AttributeBuffer
import streaming_data_types.fbschemas.histogram_hm00.BinBoundaryData as BinBoundaryDataBuffer
import streaming_data_types.fbschemas.histogram_hm00.HistogramData as HistogramDataBuffer
from streaming_data_types.fbschemas.histogram_hm00 import hm00_Array
from streaming_data_types.fbschemas.histogram_hm00.DType import DType as DT
from streaming_data_types.utils import check_schema_identifier

FILE_IDENTIFIER = b"hm00"


def get_dtype(data: numpy.ndarray | str | float | int):
    from numpy import ndarray

    if isinstance(data, ndarray):
        type_map = {
            numpy.dtype(x): d
            for x, d in (
                ("int8", DT.int8),
                ("int16", DT.int16),
                ("int32", DT.int32),
                ("int64", DT.int64),
                ("uint8", DT.uint8),
                ("uint16", DT.uint16),
                ("uint32", DT.uint32),
                ("uint64", DT.uint64),
                ("float32", DT.float32),
                ("float64", DT.float64),
            )
        }
        return type_map[data.dtype]
    if isinstance(data, str):
        return DT.c_string
    if isinstance(data, float):
        return DT.float64
    if isinstance(data, int):
        return DT.int64
    raise RuntimeError(f"Unsupported data type {type(data)} in get_dtype")


def to_buffer(data: numpy.ndarray | str | float | int):
    from struct import pack

    from numpy import frombuffer, ndarray, uint8

    if isinstance(data, ndarray):
        return data
    if isinstance(data, str):
        return frombuffer(data.encode(), uint8)
    if isinstance(data, int):
        return frombuffer(pack("q", data), uint8)
    if isinstance(data, float):
        return frombuffer(pack("d", data), uint8)
    raise RuntimeError(f"Unsupported data type {type(data)} in to_buffer")


def from_buffer(fb_array) -> numpy.ndarray:
    """Convert a flatbuffer array into the correct type"""
    raw_data = fb_array.DataAsNumpy()
    type_map = {
        d: numpy.dtype(x)
        for x, d in (
            ("int8", DT.int8),
            ("int16", DT.int16),
            ("int32", DT.int32),
            ("int64", DT.int64),
            ("uint8", DT.uint8),
            ("uint16", DT.uint16),
            ("uint32", DT.uint32),
            ("uint64", DT.uint64),
            ("float32", DT.float32),
            ("float64", DT.float64),
        )
    }
    return raw_data.view(type_map[fb_array.DataType()])


@dataclass
class Attribute:
    name: str
    data: numpy.ndarray | str | int | float
    description: str | None = None
    source: str | None = None

    def __eq__(self, other):
        if not isinstance(other, Attribute):
            return False
        data_is_equal = type(self.data) == type(other.data)  # noqa: E721
        if type(self.data) is numpy.ndarray:
            data_is_equal = data_is_equal and numpy.array_equal(self.data, other.data)
        else:
            data_is_equal = data_is_equal and self.data == other.data
        return (
            data_is_equal
            and self.name == other.name
            and self.description == other.description
            and self.source == other.source
        )

    def pack(self, builder):
        from numpy import uint8

        import streaming_data_types.fbschemas.histogram_hm00.Attribute as Buffer

        name_offset = builder.CreateString(self.name)
        description_offset = (
            None if self.description is None else builder.CreateString(self.description)
        )
        source_offset = (
            None if self.source is None else builder.CreateString(self.source)
        )
        data_offset = builder.CreateNumpyVector(
            to_buffer(self.data).flatten().view(uint8)
        )
        Buffer.AttributeStart(builder)
        Buffer.AttributeAddName(builder, name_offset)
        if description_offset is not None:
            Buffer.AttributeAddDescription(builder, description_offset)
        if source_offset is not None:
            Buffer.AttributeAddSource(builder, source_offset)
        Buffer.AttributeAddDataType(builder, get_dtype(self.data))
        Buffer.AttributeAddData(builder, data_offset)
        return Buffer.AttributeEnd(builder)

    @classmethod
    def from_buffer(cls, b: AttributeBuffer):
        data = (
            b.DataAsNumpy().tobytes().decode()
            if b.DataType() == DT.c_string
            else from_buffer(b)
        )
        if isinstance(data, numpy.ndarray) and len(data) == 1:
            if numpy.issubdtype(data.dtype, numpy.floating):
                data = float(data[0])
            elif numpy.issubdtype(data.dtype, numpy.integer):
                data = int(data[0])
        source = None if b.Source() is None else b.Source().decode()
        description = None if b.Description() is None else b.Description().decode()
        name = b.Name().decode()
        return cls(name=name, description=description, source=source, data=data)


@dataclass
class BinBoundaryData:
    name: str
    data: numpy.ndarray
    unit: str | None = None
    label: str | None = None

    def __eq__(self, other):
        if not isinstance(other, BinBoundaryData):
            return False
        same_data_type = type(self.data) == type(other.data)  # noqa: E721
        if isinstance(self.data, numpy.ndarray):
            same_data_type &= numpy.array_equal(self.data, other.data)
        else:
            same_data_type &= self.data == other.data
        return same_data_type and self.unit == other.unit and self.label == other.label

    def pack(self, builder):
        from numpy import uint8

        import streaming_data_types.fbschemas.histogram_hm00.BinBoundaryData as Buffer

        name_offset = builder.CreateString(self.name)
        unit_offset = None if self.unit is None else builder.CreateString(self.unit)
        label_offset = None if self.label is None else builder.CreateString(self.label)
        buf = to_buffer(self.data)
        data_offset = builder.CreateNumpyVector(buf.flatten().view(uint8))
        Buffer.BinBoundaryDataStart(builder)
        Buffer.BinBoundaryDataAddName(builder, name_offset)
        if unit_offset is not None:
            Buffer.BinBoundaryDataAddUnit(builder, unit_offset)
        if label_offset is not None:
            Buffer.BinBoundaryDataAddLabel(builder, label_offset)
        Buffer.BinBoundaryDataAddDataType(builder, get_dtype(self.data))
        Buffer.BinBoundaryDataAddData(builder, data_offset)
        return Buffer.BinBoundaryDataEnd(builder)

    @classmethod
    def from_buffer(cls, b: BinBoundaryDataBuffer):
        data = (
            b.DataAsNumpy().tobytes().decode()
            if b.DataType() == DT.c_string
            else from_buffer(b)
        )
        label = None if b.Label() is None else b.Label().decode()
        unit = None if b.Unit() is None else b.Unit().decode()
        name = b.Name().decode()
        return cls(name=name, unit=unit, label=label, data=data)


@dataclass
class HistogramData:
    data: numpy.ndarray | str
    unit: str | None = None

    def __eq__(self, other):
        if not isinstance(other, HistogramData):
            return False
        same_data_type = type(self.data) == type(other.data)  # noqa: E721
        if isinstance(self.data, numpy.ndarray):
            same_data_type &= numpy.array_equal(self.data, other.data)
        else:
            same_data_type &= self.data == other.data
        return same_data_type and self.unit == other.unit

    def pack(self, builder):
        from numpy import asarray, uint8

        import streaming_data_types.fbschemas.histogram_hm00.HistogramData as Buffer

        unit_offset = builder.CreateString(self.unit) if self.unit is not None else None
        buf = to_buffer(self.data)
        shape_offset = builder.CreateNumpyVector(asarray(buf.shape))
        data_offset = builder.CreateNumpyVector(buf.flatten().view(uint8))
        Buffer.HistogramDataStart(builder)
        if unit_offset is not None:
            Buffer.HistogramDataAddUnit(builder, unit_offset)
        Buffer.HistogramDataAddDataType(builder, get_dtype(self.data))
        Buffer.HistogramDataAddShape(builder, shape_offset)
        Buffer.HistogramDataAddData(builder, data_offset)
        return Buffer.HistogramDataEnd(builder)

    @classmethod
    def from_buffer(cls, b: HistogramDataBuffer):
        data = (
            b.DataAsNumpy().tobytes().decode()
            if b.DataType() == DT.c_string
            else from_buffer(b).reshape(b.ShapeAsNumpy())
        )
        unit = None if b.Unit() is None else b.Unit().decode()
        return cls(unit=unit, data=data)


def serialise_hm00(
    source_name: str,
    unique_id: int,
    timestamp: datetime,
    data: HistogramData,
    errors: HistogramData | None = None,
    dimensions: list[BinBoundaryData] | None = None,
    attributes: list[Attribute] | None = None,
) -> bytes:
    import streaming_data_types.fbschemas.histogram_hm00.hm00_Array as Buffer

    builder = flatbuffers.Builder(1024)
    builder.ForceDefaults(True)

    # Build dimensions
    temp_dimensions = (
        None if dimensions is None else [item.pack(builder) for item in dimensions]
    )
    if temp_dimensions is not None:
        Buffer.hm00_ArrayStartDimensionsVector(builder, len(dimensions))
        for item in reversed(temp_dimensions):
            builder.PrependUOffsetTRelative(item)
    dimensions_offset = None if temp_dimensions is None else builder.EndVector()

    # Build data
    data_offset = data.pack(builder)

    errors_offset = None if errors is None else errors.pack(builder)

    # Build attributes
    temp_attributes = (
        None if attributes is None else [item.pack(builder) for item in attributes]
    )
    if temp_attributes is not None:
        Buffer.hm00_ArrayStartAttributesVector(builder, len(attributes))
        for item in reversed(temp_attributes):
            builder.PrependUOffsetTRelative(item)
    attributes_offset = None if temp_attributes is None else builder.EndVector()

    source_name_offset = builder.CreateString(source_name)

    # Build the actual buffer
    Buffer.hm00_ArrayStart(builder)
    Buffer.hm00_ArrayAddSourceName(builder, source_name_offset)
    Buffer.hm00_ArrayAddId(builder, unique_id)
    Buffer.hm00_ArrayAddTimestamp(builder, int(timestamp.timestamp() * 1e9))
    if dimensions_offset is not None:
        Buffer.hm00_ArrayAddDimensions(builder, dimensions_offset)
    Buffer.hm00_ArrayAddData(builder, data_offset)
    if errors_offset is not None:
        Buffer.hm00_ArrayAddErrors(builder, errors_offset)
    if attributes_offset is not None:
        Buffer.hm00_ArrayAddAttributes(builder, attributes_offset)
    array_message = Buffer.hm00_ArrayEnd(builder)

    builder.Finish(array_message, file_identifier=FILE_IDENTIFIER)
    return bytes(builder.Output())


hm00_Array_t = NamedTuple(
    "hm00_Array",
    (
        ("source_name", str),
        ("unique_id", int),
        ("timestamp", datetime),
        ("dimensions", list[BinBoundaryData]),
        ("data", HistogramData),
        ("errors", HistogramData | None),
        ("attributes", list[Attribute]),
    ),
)


def deserialise_hm00(buffer: bytearray | bytes) -> hm00_Array:
    check_schema_identifier(buffer, FILE_IDENTIFIER)

    hm00_array = hm00_Array.hm00_Array.GetRootAs(buffer, offset=0)
    unique_id = hm00_array.Id()
    max_time = datetime(
        year=3001, month=1, day=1, hour=0, minute=0, second=0
    ).timestamp()
    used_timestamp = hm00_array.Timestamp() / 1e9
    if used_timestamp > max_time:
        used_timestamp = max_time
    dimensions = [
        BinBoundaryData.from_buffer(hm00_array.Dimensions(i))
        for i in range(hm00_array.DimensionsLength())
    ]
    data = HistogramData.from_buffer(hm00_array.Data())
    errors = (
        None
        if hm00_array.Errors() is None
        else HistogramData.from_buffer(hm00_array.Errors())
    )
    attributes = [
        Attribute.from_buffer(hm00_array.Attributes(i))
        for i in range(hm00_array.AttributesLength())
    ]

    return hm00_Array_t(
        source_name=hm00_array.SourceName().decode(),
        unique_id=unique_id,
        timestamp=datetime.fromtimestamp(used_timestamp, tz=timezone.utc),
        dimensions=dimensions,
        data=data,
        errors=errors,
        attributes=attributes,
    )