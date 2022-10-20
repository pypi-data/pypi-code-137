# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: weni/protobuf/wpp_router/channel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='weni/protobuf/wpp_router/channel.proto',
  package='weni.ai.whatsapp_router',
  syntax='proto3',
  serialized_options=b'Z\004./pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&weni/protobuf/wpp_router/channel.proto\x12\x17weni.ai.whatsapp_router\",\n\x0e\x43hannelRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\" \n\x0f\x43hannelResponse\x12\r\n\x05token\x18\x01 \x01(\t2v\n\x0e\x43hannelService\x12\x64\n\rCreateChannel\x12\'.weni.ai.whatsapp_router.ChannelRequest\x1a(.weni.ai.whatsapp_router.ChannelResponse\"\x00\x42\x06Z\x04./pbb\x06proto3'
)




_CHANNELREQUEST = _descriptor.Descriptor(
  name='ChannelRequest',
  full_name='weni.ai.whatsapp_router.ChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='weni.ai.whatsapp_router.ChannelRequest.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='weni.ai.whatsapp_router.ChannelRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=111,
)


_CHANNELRESPONSE = _descriptor.Descriptor(
  name='ChannelResponse',
  full_name='weni.ai.whatsapp_router.ChannelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='weni.ai.whatsapp_router.ChannelResponse.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['ChannelRequest'] = _CHANNELREQUEST
DESCRIPTOR.message_types_by_name['ChannelResponse'] = _CHANNELRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelRequest = _reflection.GeneratedProtocolMessageType('ChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELREQUEST,
  '__module__' : 'weni.protobuf.wpp_router.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.ai.whatsapp_router.ChannelRequest)
  })
_sym_db.RegisterMessage(ChannelRequest)

ChannelResponse = _reflection.GeneratedProtocolMessageType('ChannelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELRESPONSE,
  '__module__' : 'weni.protobuf.wpp_router.channel_pb2'
  # @@protoc_insertion_point(class_scope:weni.ai.whatsapp_router.ChannelResponse)
  })
_sym_db.RegisterMessage(ChannelResponse)


DESCRIPTOR._options = None

_CHANNELSERVICE = _descriptor.ServiceDescriptor(
  name='ChannelService',
  full_name='weni.ai.whatsapp_router.ChannelService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=147,
  serialized_end=265,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateChannel',
    full_name='weni.ai.whatsapp_router.ChannelService.CreateChannel',
    index=0,
    containing_service=None,
    input_type=_CHANNELREQUEST,
    output_type=_CHANNELRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHANNELSERVICE)

DESCRIPTOR.services_by_name['ChannelService'] = _CHANNELSERVICE

# @@protoc_insertion_point(module_scope)
