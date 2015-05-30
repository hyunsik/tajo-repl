# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PrimitiveProtos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PrimitiveProtos.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15PrimitiveProtos.proto\"\x1c\n\x0bStringProto\x12\r\n\x05value\x18\x01 \x02(\t\"\x19\n\x08IntProto\x12\r\n\x05value\x18\x01 \x02(\x05\"\x1a\n\tLongProto\x12\r\n\x05value\x18\x01 \x02(\x03\"\x1a\n\tBoolProto\x12\r\n\x05value\x18\x01 \x02(\x08\"\x0b\n\tNullProto\"!\n\x0fStringListProto\x12\x0e\n\x06values\x18\x01 \x03(\t\"+\n\rKeyValueProto\x12\x0b\n\x03key\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"2\n\x10KeyValueSetProto\x12\x1e\n\x06keyval\x18\x01 \x03(\x0b\x32\x0e.KeyValueProtoB<\n#org.apache.tajo.rpc.protocolrecordsB\x0fPrimitiveProtos\x88\x01\x01\xa0\x01\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STRINGPROTO = _descriptor.Descriptor(
  name='StringProto',
  full_name='StringProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='StringProto.value', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=53,
)


_INTPROTO = _descriptor.Descriptor(
  name='IntProto',
  full_name='IntProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='IntProto.value', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=80,
)


_LONGPROTO = _descriptor.Descriptor(
  name='LongProto',
  full_name='LongProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='LongProto.value', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=108,
)


_BOOLPROTO = _descriptor.Descriptor(
  name='BoolProto',
  full_name='BoolProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='BoolProto.value', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=136,
)


_NULLPROTO = _descriptor.Descriptor(
  name='NullProto',
  full_name='NullProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=149,
)


_STRINGLISTPROTO = _descriptor.Descriptor(
  name='StringListProto',
  full_name='StringListProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='StringListProto.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=184,
)


_KEYVALUEPROTO = _descriptor.Descriptor(
  name='KeyValueProto',
  full_name='KeyValueProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='KeyValueProto.key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='KeyValueProto.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=229,
)


_KEYVALUESETPROTO = _descriptor.Descriptor(
  name='KeyValueSetProto',
  full_name='KeyValueSetProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyval', full_name='KeyValueSetProto.keyval', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=281,
)

_KEYVALUESETPROTO.fields_by_name['keyval'].message_type = _KEYVALUEPROTO
DESCRIPTOR.message_types_by_name['StringProto'] = _STRINGPROTO
DESCRIPTOR.message_types_by_name['IntProto'] = _INTPROTO
DESCRIPTOR.message_types_by_name['LongProto'] = _LONGPROTO
DESCRIPTOR.message_types_by_name['BoolProto'] = _BOOLPROTO
DESCRIPTOR.message_types_by_name['NullProto'] = _NULLPROTO
DESCRIPTOR.message_types_by_name['StringListProto'] = _STRINGLISTPROTO
DESCRIPTOR.message_types_by_name['KeyValueProto'] = _KEYVALUEPROTO
DESCRIPTOR.message_types_by_name['KeyValueSetProto'] = _KEYVALUESETPROTO

StringProto = _reflection.GeneratedProtocolMessageType('StringProto', (_message.Message,), dict(
  DESCRIPTOR = _STRINGPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:StringProto)
  ))
_sym_db.RegisterMessage(StringProto)

IntProto = _reflection.GeneratedProtocolMessageType('IntProto', (_message.Message,), dict(
  DESCRIPTOR = _INTPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:IntProto)
  ))
_sym_db.RegisterMessage(IntProto)

LongProto = _reflection.GeneratedProtocolMessageType('LongProto', (_message.Message,), dict(
  DESCRIPTOR = _LONGPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:LongProto)
  ))
_sym_db.RegisterMessage(LongProto)

BoolProto = _reflection.GeneratedProtocolMessageType('BoolProto', (_message.Message,), dict(
  DESCRIPTOR = _BOOLPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:BoolProto)
  ))
_sym_db.RegisterMessage(BoolProto)

NullProto = _reflection.GeneratedProtocolMessageType('NullProto', (_message.Message,), dict(
  DESCRIPTOR = _NULLPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:NullProto)
  ))
_sym_db.RegisterMessage(NullProto)

StringListProto = _reflection.GeneratedProtocolMessageType('StringListProto', (_message.Message,), dict(
  DESCRIPTOR = _STRINGLISTPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:StringListProto)
  ))
_sym_db.RegisterMessage(StringListProto)

KeyValueProto = _reflection.GeneratedProtocolMessageType('KeyValueProto', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUEPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:KeyValueProto)
  ))
_sym_db.RegisterMessage(KeyValueProto)

KeyValueSetProto = _reflection.GeneratedProtocolMessageType('KeyValueSetProto', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUESETPROTO,
  __module__ = 'PrimitiveProtos_pb2'
  # @@protoc_insertion_point(class_scope:KeyValueSetProto)
  ))
_sym_db.RegisterMessage(KeyValueSetProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#org.apache.tajo.rpc.protocolrecordsB\017PrimitiveProtos\210\001\001\240\001\001'))
import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
# @@protoc_insertion_point(module_scope)
