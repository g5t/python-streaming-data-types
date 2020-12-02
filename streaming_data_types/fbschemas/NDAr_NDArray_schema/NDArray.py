# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FB_Tables

import flatbuffers


class NDArray(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsNDArray(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NDArray()
        x.Init(buf, n + offset)
        return x

    # NDArray
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NDArray
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # NDArray
    def TimeStamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float64Flags, o + self._tab.Pos
            )
        return 0.0

    # NDArray
    def EpicsTS(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from .epicsTimeStamp import epicsTimeStamp

            obj = epicsTimeStamp()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # NDArray
    def Dims(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # NDArray
    def DimsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # NDArray
    def DimsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NDArray
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # NDArray
    def PData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint8Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1),
            )
        return 0

    # NDArray
    def PDataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # NDArray
    def PDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # NDArray
    def PAttributeList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .NDAttribute import NDAttribute

            obj = NDAttribute()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # NDArray
    def PAttributeListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0


def NDArrayStart(builder):
    builder.StartObject(7)


def NDArrayAddId(builder, id):
    builder.PrependInt32Slot(0, id, 0)


def NDArrayAddTimeStamp(builder, timeStamp):
    builder.PrependFloat64Slot(1, timeStamp, 0.0)


def NDArrayAddEpicsTS(builder, epicsTS):
    builder.PrependStructSlot(
        2, flatbuffers.number_types.UOffsetTFlags.py_type(epicsTS), 0
    )


def NDArrayAddDims(builder, dims):
    builder.PrependUOffsetTRelativeSlot(
        3, flatbuffers.number_types.UOffsetTFlags.py_type(dims), 0
    )


def NDArrayStartDimsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def NDArrayAddDataType(builder, dataType):
    builder.PrependInt8Slot(4, dataType, 0)


def NDArrayAddPData(builder, pData):
    builder.PrependUOffsetTRelativeSlot(
        5, flatbuffers.number_types.UOffsetTFlags.py_type(pData), 0
    )


def NDArrayStartPDataVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)


def NDArrayAddPAttributeList(builder, pAttributeList):
    builder.PrependUOffsetTRelativeSlot(
        6, flatbuffers.number_types.UOffsetTFlags.py_type(pAttributeList), 0
    )


def NDArrayStartPAttributeListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)


def NDArrayEnd(builder):
    return builder.EndObject()
