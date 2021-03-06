# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_stream.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_stream.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63lient_stream.proto\"\x1a\n\nSimpleCall\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x0eSimpleResponse\x12\x0f\n\x07quality\x18\x01 \x01(\t2:\n\tSimpelCom\x12-\n\x0bNumberTrade\x12\x0b.SimpleCall\x1a\x0f.SimpleResponse\"\x00\x62\x06proto3'
)




_SIMPLECALL = _descriptor.Descriptor(
  name='SimpleCall',
  full_name='SimpleCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='SimpleCall.name', index=0,
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
  serialized_start=23,
  serialized_end=49,
)


_SIMPLERESPONSE = _descriptor.Descriptor(
  name='SimpleResponse',
  full_name='SimpleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='quality', full_name='SimpleResponse.quality', index=0,
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
  serialized_start=51,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['SimpleCall'] = _SIMPLECALL
DESCRIPTOR.message_types_by_name['SimpleResponse'] = _SIMPLERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleCall = _reflection.GeneratedProtocolMessageType('SimpleCall', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLECALL,
  '__module__' : 'client_stream_pb2'
  # @@protoc_insertion_point(class_scope:SimpleCall)
  })
_sym_db.RegisterMessage(SimpleCall)

SimpleResponse = _reflection.GeneratedProtocolMessageType('SimpleResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLERESPONSE,
  '__module__' : 'client_stream_pb2'
  # @@protoc_insertion_point(class_scope:SimpleResponse)
  })
_sym_db.RegisterMessage(SimpleResponse)



_SIMPELCOM = _descriptor.ServiceDescriptor(
  name='SimpelCom',
  full_name='SimpelCom',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=86,
  serialized_end=144,
  methods=[
  _descriptor.MethodDescriptor(
    name='NumberTrade',
    full_name='SimpelCom.NumberTrade',
    index=0,
    containing_service=None,
    input_type=_SIMPLECALL,
    output_type=_SIMPLERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMPELCOM)

DESCRIPTOR.services_by_name['SimpelCom'] = _SIMPELCOM

# @@protoc_insertion_point(module_scope)
