# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unary.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='unary.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bunary.proto\"<\n\nProcesData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\x02\x12\x12\n\nbrightness\x18\x03 \x01(\x02\"N\n\rProcesQuality\x12\x0f\n\x07quality\x18\x01 \x01(\t\x12\x10\n\x08\x61\x63\x63uracy\x18\x02 \x01(\x02\x12\x1a\n\x12standard_deviation\x18\x03 \x01(\x02\x32\x39\n\tSimpelCom\x12,\n\x0bNumberTrade\x12\x0b.ProcesData\x1a\x0e.ProcesQuality\"\x00\x62\x06proto3'
)




_PROCESDATA = _descriptor.Descriptor(
  name='ProcesData',
  full_name='ProcesData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ProcesData.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ProcesData.data', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brightness', full_name='ProcesData.brightness', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=15,
  serialized_end=75,
)


_PROCESQUALITY = _descriptor.Descriptor(
  name='ProcesQuality',
  full_name='ProcesQuality',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='quality', full_name='ProcesQuality.quality', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='ProcesQuality.accuracy', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='standard_deviation', full_name='ProcesQuality.standard_deviation', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=77,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['ProcesData'] = _PROCESDATA
DESCRIPTOR.message_types_by_name['ProcesQuality'] = _PROCESQUALITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcesData = _reflection.GeneratedProtocolMessageType('ProcesData', (_message.Message,), {
  'DESCRIPTOR' : _PROCESDATA,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:ProcesData)
  })
_sym_db.RegisterMessage(ProcesData)

ProcesQuality = _reflection.GeneratedProtocolMessageType('ProcesQuality', (_message.Message,), {
  'DESCRIPTOR' : _PROCESQUALITY,
  '__module__' : 'unary_pb2'
  # @@protoc_insertion_point(class_scope:ProcesQuality)
  })
_sym_db.RegisterMessage(ProcesQuality)



_SIMPELCOM = _descriptor.ServiceDescriptor(
  name='SimpelCom',
  full_name='SimpelCom',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=157,
  serialized_end=214,
  methods=[
  _descriptor.MethodDescriptor(
    name='NumberTrade',
    full_name='SimpelCom.NumberTrade',
    index=0,
    containing_service=None,
    input_type=_PROCESDATA,
    output_type=_PROCESQUALITY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPELCOM)

DESCRIPTOR.services_by_name['SimpelCom'] = _SIMPELCOM

# @@protoc_insertion_point(module_scope)
