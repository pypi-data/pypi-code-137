# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2022-10-17 22:48
# cython: language_level=2

from capnpy import ptr as _ptr
from capnpy.struct_ import Struct as _Struct
from capnpy.struct_ import check_tag as _check_tag
from capnpy.struct_ import undefined as _undefined
from capnpy.enum import enum as _enum, fill_enum as _fill_enum
from capnpy.enum import BaseEnum as _BaseEnum
from capnpy.type import Types as _Types
from capnpy.segment.segment import Segment as _Segment
from capnpy.segment.segment import MultiSegment as _MultiSegment
from capnpy.segment.builder import SegmentBuilder as _SegmentBuilder
from capnpy.list import List as _List
from capnpy.list import PrimitiveItemType as _PrimitiveItemType
from capnpy.list import BoolItemType as _BoolItemType
from capnpy.list import TextItemType as _TextItemType
from capnpy.list import TextUnicodeItemType as _TextUnicodeItemType
from capnpy.list import StructItemType as _StructItemType
from capnpy.list import EnumItemType as _EnumItemType
from capnpy.list import VoidItemType as _VoidItemType
from capnpy.list import ListItemType as _ListItemType
from capnpy.anypointer import AnyPointer as _AnyPointer
from capnpy.util import text_bytes_repr as _text_bytes_repr
from capnpy.util import text_unicode_repr as _text_unicode_repr
from capnpy.util import data_repr as _data_repr
from capnpy.util import float32_repr as _float32_repr
from capnpy.util import float64_repr as _float64_repr
from capnpy.util import extend_module_maybe as _extend_module_maybe
from capnpy.util import check_version as _check_version
from capnpy.util import encode_maybe as _encode_maybe
__capnpy_id__ = 0xb8641e621253ede2
__capnpy_version__ = '0.9.0'
__capnproto_version__ = '0.9.1'
_check_version(__name__, __capnpy_version__)
from capnpy.schema import CodeGeneratorRequest as _CodeGeneratorRequest
from capnpy.annotate import Options as _Options
from capnpy.reflection import ReflectionData as _ReflectionData
class _plexo_promise_ReflectionData(_ReflectionData):
    request = _CodeGeneratorRequest.from_buffer(_Segment(b'\x00\x00\x00\x00\x00\x00\x04\x00\x11\x00\x00\x00\xb7\x00\x00\x00u\x02\x00\x00\x1f\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x005\x02\x00\x007\x00\x00\x00\x00\x00\t\x01\x00\x00\x00\x00\x08\x00\x00\x00\x05\x00\x06\x00\xe2\xedS\x12b\x1ed\xb8\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x00\x00\x00*\x01\x00\x00Q\x00\x00\x00\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x14\x15\x04\xfd\xe8\xdc\xe7%\x00\x00\x00\x01\x00\x04\x00\xe2\xedS\x12b\x1ed\xb8\x02\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00=\x00\x00\x00\x92\x01\x00\x00U\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Q\x00\x00\x00W\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00src/plexo/schema/plexo_promise.capnp\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x01\x00\xf0\x14\x15\x04\xfd\xe8\xdc\xe7\x01\x00\x00\x00j\x00\x00\x00PlexoPromise\x00\x00\x00\x00src/plexo/schema/plexo_promise.capnp:PlexoPromise\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x18\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x99\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x98\x00\x00\x00\x03\x00\x01\x00\xa4\x00\x00\x00\x02\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa1\x00\x00\x00Z\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x03\x00\x01\x00\xac\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa9\x00\x00\x00J\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa8\x00\x00\x00\x03\x00\x01\x00\xb4\x00\x00\x00\x02\x00\x01\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb1\x00\x00\x00\x9a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb4\x00\x00\x00\x03\x00\x01\x00\xc0\x00\x00\x00\x02\x00\x01\x00\x04\x00\x00\x00\x03\x00\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbd\x00\x00\x00\x9a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\x00\x03\x00\x01\x00\xcc\x00\x00\x00\x02\x00\x01\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc8\x00\x00\x00\x03\x00\x01\x00\xd4\x00\x00\x00\x02\x00\x01\x00instanceId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00proposalId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00typeName\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00acceptedInstanceId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00acceptedProposalId\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00multicastIp\x00\x00\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x01\x00\x02\x00\xf0\x14\x15\x04\xfd\xe8\xdc\xe7\x00\x00\x00\x00\x00\x00\x00\x00\r\x00\x00\x007\x00\x00\x00\xe2\xedS\x12b\x1ed\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x02\x00\xe2\xedS\x12b\x1ed\xb8\x05\x00\x00\x00*\x01\x00\x00\x15\x00\x00\x00\x07\x00\x00\x00src/plexo/schema/plexo_promise.capnp\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00'), 8, 0, 4)
    default_options = _Options.from_buffer(_Segment(b'\x03\x00\x03\x00\x01\x00\x03\x00'), 0, 1, 0)
    pyx = False
_reflection_data = _plexo_promise_ReflectionData()

#### FORWARD DECLARATIONS ####

class PlexoPromise(_Struct): pass
PlexoPromise.__name__ = 'PlexoPromise'


#### DEFINITIONS ####

@PlexoPromise.__extend__
class PlexoPromise(_Struct):
    __capnpy_id__ = 0xe7dce8fd041514f0
    __static_data_size__ = 4
    __static_ptrs_size__ = 2
    
    
    @property
    def instance_id(self):
        # no union check
        value = self._read_primitive(0, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def proposal_id(self):
        # no union check
        value = self._read_primitive(8, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def type_name(self):
        # no union check
        return self._read_text_bytes(0)
    
    def get_type_name(self):
        return self._read_text_bytes(0, default_=b"")
    
    def has_type_name(self):
        ptr = self._read_fast_ptr(0)
        return ptr != 0
    
    @property
    def accepted_instance_id(self):
        # no union check
        value = self._read_primitive(16, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def accepted_proposal_id(self):
        # no union check
        value = self._read_primitive(24, ord(b'Q'))
        if 0 != 0:
            value = value ^ 0
        return value
    
    @property
    def multicast_ip(self):
        # no union check
        return self._read_data(8)
    
    def get_multicast_ip(self):
        return self._read_data(8, default_=b"")
    
    def has_multicast_ip(self):
        ptr = self._read_fast_ptr(8)
        return ptr != 0
    
    @staticmethod
    def __new(instance_id=0, proposal_id=0, type_name=None, accepted_instance_id=0, accepted_proposal_id=0, multicast_ip=None):
        builder = _SegmentBuilder()
        pos = builder.allocate(48)
        builder.write_uint64(pos + 0, instance_id)
        builder.write_uint64(pos + 8, proposal_id)
        builder.alloc_text(pos + 32, type_name)
        builder.write_uint64(pos + 16, accepted_instance_id)
        builder.write_uint64(pos + 24, accepted_proposal_id)
        builder.alloc_data(pos + 40, multicast_ip)
        return builder.as_string()
    
    def __init__(self, instance_id=0, proposal_id=0, type_name=None, accepted_instance_id=0, accepted_proposal_id=0, multicast_ip=None):
        _buf = PlexoPromise.__new(instance_id, proposal_id, type_name, accepted_instance_id, accepted_proposal_id, multicast_ip)
        self._init_from_buffer(_buf, 0, 4, 2)
    
    def shortrepr(self):
        parts = []
        parts.append("instanceId = %s" % self.instance_id)
        parts.append("proposalId = %s" % self.proposal_id)
        if self.has_type_name(): parts.append("typeName = %s" % _text_bytes_repr(self.get_type_name()))
        parts.append("acceptedInstanceId = %s" % self.accepted_instance_id)
        parts.append("acceptedProposalId = %s" % self.accepted_proposal_id)
        if self.has_multicast_ip(): parts.append("multicastIp = %s" % _data_repr(self.get_multicast_ip()))
        return "(%s)" % ", ".join(parts)

_PlexoPromise_list_item_type = _StructItemType(PlexoPromise)


_extend_module_maybe(globals(), modname=__name__)