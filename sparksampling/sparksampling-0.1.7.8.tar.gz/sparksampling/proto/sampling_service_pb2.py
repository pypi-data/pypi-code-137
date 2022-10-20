# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sampling_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16sampling_service.proto\"\xea\x01\n\x0fSamplingRequest\x12,\n\x0fsampling_method\x18\x01 \x01(\x0e\x32\x13.SamplingMethodType\x12$\n\x0b\x66ile_format\x18\x02 \x01(\x0e\x32\x0f.FileFormatType\x12$\n\rsampling_conf\x18\x03 \x01(\x0b\x32\r.SamplingConf\x12$\n\x0b\x66ormat_conf\x18\x04 \x01(\x0b\x32\x0f.FileFormatConf\x12\x12\n\ninput_path\x18\x05 \x01(\t\x12\x13\n\x0boutput_path\x18\x06 \x01(\t\x12\x0e\n\x06job_id\x18\x07 \x01(\t\"\x1f\n\rCancelRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\t\"/\n\x0e\x43\x61ncelResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xaf\x01\n\x10SamplingResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12,\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1e.SamplingResponse.ResponseData\x1aN\n\x0cResponseData\x12(\n\x0eparent_request\x18\x01 \x01(\x0b\x32\x10.SamplingRequest\x12\x14\n\x0csampled_path\x18\x02 \x01(\t\"#\n\x04\x64ict\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xbe\x01\n\x0cSamplingConf\x12\x10\n\x08\x66raction\x18\x01 \x01(\t\x12\x18\n\x10with_replacement\x18\x02 \x01(\x08\x12\x0c\n\x04seed\x18\x03 \x01(\r\x12\x16\n\x0estratified_key\x18\x04 \x01(\t\x12\r\n\x05\x63ount\x18\x05 \x01(\r\x12\x14\n\x0csampling_col\x18\x06 \x03(\t\x12\x10\n\x08group_by\x18\x07 \x01(\t\x12\x11\n\tgroup_num\x18\x08 \x01(\r\x12\x12\n\nensure_col\x18\t \x01(\x08\"2\n\x0e\x46ileFormatConf\x12\x13\n\x0bwith_header\x18\x01 \x01(\x08\x12\x0b\n\x03sep\x18\x02 \x01(\t\"\xb0\x08\n\x17RelationSamplingRequest\x12?\n\x0fsampling_stages\x18\x01 \x03(\x0b\x32&.RelationSamplingRequest.SamplingStage\x12?\n\x0frelation_stages\x18\x02 \x03(\x0b\x32&.RelationSamplingRequest.RelationStage\x12\x0e\n\x06job_id\x18\x03 \x01(\t\x12\x34\n\x17\x64\x65\x66\x61ult_sampling_method\x18\x04 \x01(\x0e\x32\x13.SamplingMethodType\x12,\n\x15\x64\x65\x66\x61ult_sampling_conf\x18\x05 \x01(\x0b\x32\r.SamplingConf\x12,\n\x13\x64\x65\x66\x61ult_file_format\x18\x06 \x01(\x0e\x32\x0f.FileFormatType\x12,\n\x13\x64\x65\x66\x61ult_format_conf\x18\x07 \x01(\x0b\x32\x0f.FileFormatConf\x12\x0f\n\x07\x64ry_run\x18\x08 \x01(\x08\x1a\x8e\x02\n\rSamplingStage\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x12\n\ninput_name\x18\x02 \x01(\t\x12\x13\n\x0boutput_path\x18\x03 \x01(\t\x12\x12\n\noutput_col\x18\x04 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12,\n\x0fsampling_method\x18\x06 \x01(\x0e\x32\x13.SamplingMethodType\x12$\n\rsampling_conf\x18\x07 \x01(\x0b\x32\r.SamplingConf\x12$\n\x0b\x66ile_format\x18\x08 \x01(\x0e\x32\x0f.FileFormatType\x12$\n\x0b\x66ormat_conf\x18\t \x01(\x0b\x32\x0f.FileFormatConf\x1a\xad\x01\n\x08Relation\x12\x15\n\rrelation_path\x18\x01 \x01(\t\x12\x15\n\rrelation_name\x18\x02 \x01(\t\x12\x14\n\x0crelation_col\x18\x03 \x01(\t\x12\x11\n\tinput_col\x18\x04 \x01(\t\x12$\n\x0b\x66ile_format\x18\x05 \x01(\x0e\x32\x0f.FileFormatType\x12$\n\x0b\x66ormat_conf\x18\x06 \x01(\x0b\x32\x0f.FileFormatConf\x1a\xf0\x01\n\rRelationStage\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x12\n\ninput_name\x18\x02 \x01(\t\x12\x13\n\x0boutput_path\x18\x03 \x01(\t\x12\x12\n\noutput_col\x18\x04 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x34\n\trelations\x18\x06 \x03(\x0b\x32!.RelationSamplingRequest.Relation\x12$\n\x0b\x66ile_format\x18\x07 \x01(\x0e\x32\x0f.FileFormatType\x12$\n\x0b\x66ormat_conf\x18\x08 \x01(\x0b\x32\x0f.FileFormatConf\"\x9e\x02\n\x18RelationSamplingResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x34\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32&.RelationSamplingResponse.ResponseData\x1a\x32\n\x0cSampleResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0csampled_path\x18\x02 \x01(\t\x1ay\n\x0cResponseData\x12\x30\n\x0eparent_request\x18\x01 \x01(\x0b\x32\x18.RelationSamplingRequest\x12\x37\n\x07results\x18\x02 \x03(\x0b\x32&.RelationSamplingResponse.SampleResult*\x9d\x01\n\x12SamplingMethodType\x12\x12\n\x0eUNKNOWN_METHOD\x10\x00\x12\x1a\n\x16RANDOM_SAMPLING_METHOD\x10\x01\x12\x1e\n\x1aSTRATIFIED_SAMPLING_METHOD\x10\x02\x12\x1a\n\x16SIMPLE_SAMPLING_METHOD\x10\x03\x12\x1b\n\x17\x43LUSTER_SAMPLING_METHOD\x10\x04*9\n\x0e\x46ileFormatType\x12\x12\n\x0eUNKNOWN_FORMAT\x10\x00\x12\x13\n\x0f\x46ILE_FORMAT_CSV\x10\x01\x32\xca\x01\n\x14SparkSamplingService\x12\x34\n\x0bSamplingJob\x12\x10.SamplingRequest\x1a\x11.SamplingResponse\"\x00\x12L\n\x13RelationSamplingJob\x12\x18.RelationSamplingRequest\x1a\x19.RelationSamplingResponse\"\x00\x12.\n\tCancelJob\x12\x0e.CancelRequest\x1a\x0f.CancelResponse\"\x00\x62\x06proto3')

_SAMPLINGMETHODTYPE = DESCRIPTOR.enum_types_by_name['SamplingMethodType']
SamplingMethodType = enum_type_wrapper.EnumTypeWrapper(_SAMPLINGMETHODTYPE)
_FILEFORMATTYPE = DESCRIPTOR.enum_types_by_name['FileFormatType']
FileFormatType = enum_type_wrapper.EnumTypeWrapper(_FILEFORMATTYPE)
UNKNOWN_METHOD = 0
RANDOM_SAMPLING_METHOD = 1
STRATIFIED_SAMPLING_METHOD = 2
SIMPLE_SAMPLING_METHOD = 3
CLUSTER_SAMPLING_METHOD = 4
UNKNOWN_FORMAT = 0
FILE_FORMAT_CSV = 1


_SAMPLINGREQUEST = DESCRIPTOR.message_types_by_name['SamplingRequest']
_CANCELREQUEST = DESCRIPTOR.message_types_by_name['CancelRequest']
_CANCELRESPONSE = DESCRIPTOR.message_types_by_name['CancelResponse']
_SAMPLINGRESPONSE = DESCRIPTOR.message_types_by_name['SamplingResponse']
_SAMPLINGRESPONSE_RESPONSEDATA = _SAMPLINGRESPONSE.nested_types_by_name['ResponseData']
_DICT = DESCRIPTOR.message_types_by_name['dict']
_SAMPLINGCONF = DESCRIPTOR.message_types_by_name['SamplingConf']
_FILEFORMATCONF = DESCRIPTOR.message_types_by_name['FileFormatConf']
_RELATIONSAMPLINGREQUEST = DESCRIPTOR.message_types_by_name['RelationSamplingRequest']
_RELATIONSAMPLINGREQUEST_SAMPLINGSTAGE = _RELATIONSAMPLINGREQUEST.nested_types_by_name['SamplingStage']
_RELATIONSAMPLINGREQUEST_RELATION = _RELATIONSAMPLINGREQUEST.nested_types_by_name['Relation']
_RELATIONSAMPLINGREQUEST_RELATIONSTAGE = _RELATIONSAMPLINGREQUEST.nested_types_by_name['RelationStage']
_RELATIONSAMPLINGRESPONSE = DESCRIPTOR.message_types_by_name['RelationSamplingResponse']
_RELATIONSAMPLINGRESPONSE_SAMPLERESULT = _RELATIONSAMPLINGRESPONSE.nested_types_by_name['SampleResult']
_RELATIONSAMPLINGRESPONSE_RESPONSEDATA = _RELATIONSAMPLINGRESPONSE.nested_types_by_name['ResponseData']
SamplingRequest = _reflection.GeneratedProtocolMessageType('SamplingRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLINGREQUEST,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:SamplingRequest)
  })
_sym_db.RegisterMessage(SamplingRequest)

CancelRequest = _reflection.GeneratedProtocolMessageType('CancelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELREQUEST,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:CancelRequest)
  })
_sym_db.RegisterMessage(CancelRequest)

CancelResponse = _reflection.GeneratedProtocolMessageType('CancelResponse', (_message.Message,), {
  'DESCRIPTOR' : _CANCELRESPONSE,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:CancelResponse)
  })
_sym_db.RegisterMessage(CancelResponse)

SamplingResponse = _reflection.GeneratedProtocolMessageType('SamplingResponse', (_message.Message,), {

  'ResponseData' : _reflection.GeneratedProtocolMessageType('ResponseData', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLINGRESPONSE_RESPONSEDATA,
    '__module__' : 'sampling_service_pb2'
    # @@protoc_insertion_point(class_scope:SamplingResponse.ResponseData)
    })
  ,
  'DESCRIPTOR' : _SAMPLINGRESPONSE,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:SamplingResponse)
  })
_sym_db.RegisterMessage(SamplingResponse)
_sym_db.RegisterMessage(SamplingResponse.ResponseData)

dict = _reflection.GeneratedProtocolMessageType('dict', (_message.Message,), {
  'DESCRIPTOR' : _DICT,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:dict)
  })
_sym_db.RegisterMessage(dict)

SamplingConf = _reflection.GeneratedProtocolMessageType('SamplingConf', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLINGCONF,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:SamplingConf)
  })
_sym_db.RegisterMessage(SamplingConf)

FileFormatConf = _reflection.GeneratedProtocolMessageType('FileFormatConf', (_message.Message,), {
  'DESCRIPTOR' : _FILEFORMATCONF,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:FileFormatConf)
  })
_sym_db.RegisterMessage(FileFormatConf)

RelationSamplingRequest = _reflection.GeneratedProtocolMessageType('RelationSamplingRequest', (_message.Message,), {

  'SamplingStage' : _reflection.GeneratedProtocolMessageType('SamplingStage', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONSAMPLINGREQUEST_SAMPLINGSTAGE,
    '__module__' : 'sampling_service_pb2'
    # @@protoc_insertion_point(class_scope:RelationSamplingRequest.SamplingStage)
    })
  ,

  'Relation' : _reflection.GeneratedProtocolMessageType('Relation', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONSAMPLINGREQUEST_RELATION,
    '__module__' : 'sampling_service_pb2'
    # @@protoc_insertion_point(class_scope:RelationSamplingRequest.Relation)
    })
  ,

  'RelationStage' : _reflection.GeneratedProtocolMessageType('RelationStage', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONSAMPLINGREQUEST_RELATIONSTAGE,
    '__module__' : 'sampling_service_pb2'
    # @@protoc_insertion_point(class_scope:RelationSamplingRequest.RelationStage)
    })
  ,
  'DESCRIPTOR' : _RELATIONSAMPLINGREQUEST,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:RelationSamplingRequest)
  })
_sym_db.RegisterMessage(RelationSamplingRequest)
_sym_db.RegisterMessage(RelationSamplingRequest.SamplingStage)
_sym_db.RegisterMessage(RelationSamplingRequest.Relation)
_sym_db.RegisterMessage(RelationSamplingRequest.RelationStage)

RelationSamplingResponse = _reflection.GeneratedProtocolMessageType('RelationSamplingResponse', (_message.Message,), {

  'SampleResult' : _reflection.GeneratedProtocolMessageType('SampleResult', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONSAMPLINGRESPONSE_SAMPLERESULT,
    '__module__' : 'sampling_service_pb2'
    # @@protoc_insertion_point(class_scope:RelationSamplingResponse.SampleResult)
    })
  ,

  'ResponseData' : _reflection.GeneratedProtocolMessageType('ResponseData', (_message.Message,), {
    'DESCRIPTOR' : _RELATIONSAMPLINGRESPONSE_RESPONSEDATA,
    '__module__' : 'sampling_service_pb2'
    # @@protoc_insertion_point(class_scope:RelationSamplingResponse.ResponseData)
    })
  ,
  'DESCRIPTOR' : _RELATIONSAMPLINGRESPONSE,
  '__module__' : 'sampling_service_pb2'
  # @@protoc_insertion_point(class_scope:RelationSamplingResponse)
  })
_sym_db.RegisterMessage(RelationSamplingResponse)
_sym_db.RegisterMessage(RelationSamplingResponse.SampleResult)
_sym_db.RegisterMessage(RelationSamplingResponse.ResponseData)

_SPARKSAMPLINGSERVICE = DESCRIPTOR.services_by_name['SparkSamplingService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SAMPLINGMETHODTYPE._serialized_start=2170
  _SAMPLINGMETHODTYPE._serialized_end=2327
  _FILEFORMATTYPE._serialized_start=2329
  _FILEFORMATTYPE._serialized_end=2386
  _SAMPLINGREQUEST._serialized_start=27
  _SAMPLINGREQUEST._serialized_end=261
  _CANCELREQUEST._serialized_start=263
  _CANCELREQUEST._serialized_end=294
  _CANCELRESPONSE._serialized_start=296
  _CANCELRESPONSE._serialized_end=343
  _SAMPLINGRESPONSE._serialized_start=346
  _SAMPLINGRESPONSE._serialized_end=521
  _SAMPLINGRESPONSE_RESPONSEDATA._serialized_start=443
  _SAMPLINGRESPONSE_RESPONSEDATA._serialized_end=521
  _DICT._serialized_start=523
  _DICT._serialized_end=558
  _SAMPLINGCONF._serialized_start=561
  _SAMPLINGCONF._serialized_end=751
  _FILEFORMATCONF._serialized_start=753
  _FILEFORMATCONF._serialized_end=803
  _RELATIONSAMPLINGREQUEST._serialized_start=806
  _RELATIONSAMPLINGREQUEST._serialized_end=1878
  _RELATIONSAMPLINGREQUEST_SAMPLINGSTAGE._serialized_start=1189
  _RELATIONSAMPLINGREQUEST_SAMPLINGSTAGE._serialized_end=1459
  _RELATIONSAMPLINGREQUEST_RELATION._serialized_start=1462
  _RELATIONSAMPLINGREQUEST_RELATION._serialized_end=1635
  _RELATIONSAMPLINGREQUEST_RELATIONSTAGE._serialized_start=1638
  _RELATIONSAMPLINGREQUEST_RELATIONSTAGE._serialized_end=1878
  _RELATIONSAMPLINGRESPONSE._serialized_start=1881
  _RELATIONSAMPLINGRESPONSE._serialized_end=2167
  _RELATIONSAMPLINGRESPONSE_SAMPLERESULT._serialized_start=1994
  _RELATIONSAMPLINGRESPONSE_SAMPLERESULT._serialized_end=2044
  _RELATIONSAMPLINGRESPONSE_RESPONSEDATA._serialized_start=2046
  _RELATIONSAMPLINGRESPONSE_RESPONSEDATA._serialized_end=2167
  _SPARKSAMPLINGSERVICE._serialized_start=2389
  _SPARKSAMPLINGSERVICE._serialized_end=2591
# @@protoc_insertion_point(module_scope)
