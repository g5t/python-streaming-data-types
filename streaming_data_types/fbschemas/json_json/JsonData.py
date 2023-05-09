# automatically generated by the FlatBuffers compiler, do not modify

# namespace:

import flatbuffers
from flatbuffers.compat import import_numpy

np = import_numpy()


class JsonData(object):
    __slots__ = ["_tab"]

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = JsonData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsJsonData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)

    @classmethod
    def JsonDataBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(
            buf, offset, b"\x6A\x73\x6F\x6E", size_prefixed=size_prefixed
        )

    # JsonData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # JsonData
    def Json(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None


def JsonDataStart(builder):
    builder.StartObject(1)


def Start(builder):
    JsonDataStart(builder)


def JsonDataAddJson(builder, json):
    builder.PrependUOffsetTRelativeSlot(
        0, flatbuffers.number_types.UOffsetTFlags.py_type(json), 0
    )


def AddJson(builder: flatbuffers.Builder, json: int):
    JsonDataAddJson(builder, json)


def JsonDataEnd(builder):
    return builder.EndObject()


def End(builder):
    return JsonDataEnd(builder)
