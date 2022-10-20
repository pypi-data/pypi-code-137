# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_lite_support/cc/task/core/proto/external_file.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_lite_support/cc/task/core/proto/external_file.proto',
  package='tflite.task.core',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>tensorflow_lite_support/cc/task/core/proto/external_file.proto\x12\x10tflite.task.core\"\x81\x01\n\x0c\x45xternalFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x14\n\x0c\x66ile_content\x18\x02 \x01(\x0c\x12\x42\n\x14\x66ile_descriptor_meta\x18\x04 \x01(\x0b\x32$.tflite.task.core.FileDescriptorMetaJ\x04\x08\x03\x10\x04\"@\n\x12\x46ileDescriptorMeta\x12\n\n\x02\x66\x64\x18\x01 \x01(\x05\x12\x0e\n\x06length\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03'
)




_EXTERNALFILE = _descriptor.Descriptor(
  name='ExternalFile',
  full_name='tflite.task.core.ExternalFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='tflite.task.core.ExternalFile.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_content', full_name='tflite.task.core.ExternalFile.file_content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_descriptor_meta', full_name='tflite.task.core.ExternalFile.file_descriptor_meta', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=214,
)


_FILEDESCRIPTORMETA = _descriptor.Descriptor(
  name='FileDescriptorMeta',
  full_name='tflite.task.core.FileDescriptorMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fd', full_name='tflite.task.core.FileDescriptorMeta.fd', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='tflite.task.core.FileDescriptorMeta.length', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='tflite.task.core.FileDescriptorMeta.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=280,
)

_EXTERNALFILE.fields_by_name['file_descriptor_meta'].message_type = _FILEDESCRIPTORMETA
DESCRIPTOR.message_types_by_name['ExternalFile'] = _EXTERNALFILE
DESCRIPTOR.message_types_by_name['FileDescriptorMeta'] = _FILEDESCRIPTORMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExternalFile = _reflection.GeneratedProtocolMessageType('ExternalFile', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALFILE,
  '__module__' : 'tensorflow_lite_support.cc.task.core.proto.external_file_pb2'
  # @@protoc_insertion_point(class_scope:tflite.task.core.ExternalFile)
  })
_sym_db.RegisterMessage(ExternalFile)

FileDescriptorMeta = _reflection.GeneratedProtocolMessageType('FileDescriptorMeta', (_message.Message,), {
  'DESCRIPTOR' : _FILEDESCRIPTORMETA,
  '__module__' : 'tensorflow_lite_support.cc.task.core.proto.external_file_pb2'
  # @@protoc_insertion_point(class_scope:tflite.task.core.FileDescriptorMeta)
  })
_sym_db.RegisterMessage(FileDescriptorMeta)


# @@protoc_insertion_point(module_scope)
