# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FB_Tables

import flatbuffers


class epicsTimeStamp(object):
    __slots__ = ["_tab"]

    # epicsTimeStamp
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # epicsTimeStamp
    def SecPastEpoch(self):
        return self._tab.Get(
            flatbuffers.number_types.Int32Flags,
            self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0),
        )

    # epicsTimeStamp
    def Nsec(self):
        return self._tab.Get(
            flatbuffers.number_types.Int32Flags,
            self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4),
        )


def CreateepicsTimeStamp(builder, secPastEpoch, nsec):
    builder.Prep(4, 8)
    builder.PrependInt32(nsec)
    builder.PrependInt32(secPastEpoch)
    return builder.Offset()
