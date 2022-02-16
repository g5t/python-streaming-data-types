# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class SampleEnvironmentData(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAsSampleEnvironmentData(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SampleEnvironmentData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SampleEnvironmentDataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x73\x65\x6E\x76", size_prefixed=size_prefixed
        )

    # SampleEnvironmentData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SampleEnvironmentData
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # SampleEnvironmentData
    def Channel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # SampleEnvironmentData
    def PacketTimestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags, o + self._tab.Pos
            )
        return 0

    # SampleEnvironmentData
    def TimeDelta(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Float64Flags, o + self._tab.Pos
            )
        return 0.0

    # SampleEnvironmentData
    def TimestampLocation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # SampleEnvironmentData
    def ValuesType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # SampleEnvironmentData
    def Values(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            from flatbuffers.table import Table

            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # SampleEnvironmentData
    def Timestamps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags,
                a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8),
            )
        return 0

    # SampleEnvironmentData
    def TimestampsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # SampleEnvironmentData
    def TimestampsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # SampleEnvironmentData
    def TimestampsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        return o == 0

    # SampleEnvironmentData
    def MessageCounter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(
                flatbuffers.number_types.Uint64Flags, o + self._tab.Pos
            )
        return 0


def SampleEnvironmentDataStart(builder):
    builder.StartObject(9)


def SampleEnvironmentDataAddName(builder, Name):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(Name), 0
    )


def SampleEnvironmentDataAddChannel(builder, Channel):
    builder.PrependInt32Slot(1, Channel, 0)


def SampleEnvironmentDataAddPacketTimestamp(builder, PacketTimestamp):
    builder.PrependUint64Slot(2, PacketTimestamp, 0)


def SampleEnvironmentDataAddTimeDelta(builder, TimeDelta):
    builder.PrependFloat64Slot(3, TimeDelta, 0.0)


def SampleEnvironmentDataAddTimestampLocation(builder, TimestampLocation):
    builder.PrependInt8Slot(4, TimestampLocation, 0)


def SampleEnvironmentDataAddValuesType(builder, ValuesType):
    builder.PrependUint8Slot(5, ValuesType, 0)


def SampleEnvironmentDataAddValues(builder, Values):
    builder.PrependUOffsetTRelativeSlot(
        6, flatbuffers.number_types.UOffsetTFlags.py_type(Values), 0
    )


def SampleEnvironmentDataAddTimestamps(builder, Timestamps):
    builder.PrependUOffsetTRelativeSlot(
        7, flatbuffers.number_types.UOffsetTFlags.py_type(Timestamps), 0
    )


def SampleEnvironmentDataStartTimestampsVector(builder, numElems):
    return builder.StartVector(8, numElems, 8)


def SampleEnvironmentDataAddMessageCounter(builder, MessageCounter):
    builder.PrependUint64Slot(8, MessageCounter, 0)


def SampleEnvironmentDataEnd(builder):
    return builder.EndObject()
