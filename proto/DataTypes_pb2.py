# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataTypes.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DataTypes.proto',
  package='',
  serialized_pb='\n\x0f\x44\x61taTypes.proto\"X\n\x08\x44\x61taType\x12\x13\n\x04type\x18\x01 \x02(\x0e\x32\x05.Type\x12\x0e\n\x06length\x18\x02 \x01(\x05\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x19\n\x11num_nested_fields\x18\x04 \x01(\x05*\xb9\x06\n\x04Type\x12\r\n\tNULL_TYPE\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\x08\n\x04INT1\x10\x02\x12\x08\n\x04INT2\x10\x03\x12\x08\n\x04INT4\x10\x04\x12\x08\n\x04INT8\x10\x05\x12\t\n\x05UINT1\x10\x06\x12\t\n\x05UINT2\x10\x07\x12\t\n\x05UINT4\x10\x08\x12\t\n\x05UINT8\x10\t\x12\n\n\x06\x46LOAT4\x10\n\x12\n\n\x06\x46LOAT8\x10\x0b\x12\x0b\n\x07NUMERIC\x10\x0c\x12\x08\n\x04\x43HAR\x10\x15\x12\t\n\x05NCHAR\x10\x16\x12\x0b\n\x07VARCHAR\x10\x17\x12\x0c\n\x08NVARCHAR\x10\x18\x12\x08\n\x04TEXT\x10\x19\x12\x08\n\x04\x44\x41TE\x10\x1f\x12\x08\n\x04TIME\x10 \x12\t\n\x05TIMEZ\x10!\x12\r\n\tTIMESTAMP\x10\"\x12\x0e\n\nTIMESTAMPZ\x10#\x12\x0c\n\x08INTERVAL\x10$\x12\x07\n\x03\x42IT\x10)\x12\n\n\x06VARBIT\x10*\x12\n\n\x06\x42INARY\x10+\x12\r\n\tVARBINARY\x10,\x12\x08\n\x04\x42LOB\x10-\x12\n\n\x06RECORD\x10\x33\x12\x07\n\x03\x41NY\x10=\x12\x07\n\x03UDT\x10>\x12\x0c\n\x08PROTOBUF\x10?\x12\t\n\x05INET4\x10[\x12\t\n\x05INET6\x10\\\x12\x11\n\rBOOLEAN_ARRAY\x10\x65\x12\x0e\n\nINT1_ARRAY\x10\x66\x12\x0e\n\nINT2_ARRAY\x10g\x12\x0e\n\nINT4_ARRAY\x10h\x12\x0e\n\nINT8_ARRAY\x10i\x12\x0f\n\x0bUINT1_ARRAY\x10j\x12\x0f\n\x0bUINT2_ARRAY\x10k\x12\x0f\n\x0bUINT4_ARRAY\x10l\x12\x0f\n\x0bUINT8_ARRAY\x10m\x12\x10\n\x0c\x46LOAT4_ARRAY\x10n\x12\x10\n\x0c\x46LOAT8_ARRAY\x10o\x12\x11\n\rNUMERIC_ARRAY\x10p\x12\x0e\n\nCHAR_ARRAY\x10y\x12\x0f\n\x0bNCHAR_ARRAY\x10z\x12\x11\n\rVARCHAR_ARRAY\x10{\x12\x12\n\x0eNVARCHAR_ARRAY\x10|\x12\x0e\n\nTEXT_ARRAY\x10}\x12\x0f\n\nDATE_ARRAY\x10\x83\x01\x12\x0f\n\nTIME_ARRAY\x10\x84\x01\x12\x10\n\x0bTIMEZ_ARRAY\x10\x85\x01\x12\x14\n\x0fTIMESTAMP_ARRAY\x10\x86\x01\x12\x15\n\x10TIMESTAMPZ_ARRAY\x10\x87\x01\x12\x13\n\x0eINTERVAL_ARRAY\x10\x88\x01\x42/\n\x16org.apache.tajo.commonB\rTajoDataTypesH\x01\x88\x01\x00\xa0\x01\x01')

_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NULL_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT1', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT2', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT4', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT8', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT1', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT2', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT4', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT4', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT8', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMERIC', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAR', index=13, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NCHAR', index=14, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARCHAR', index=15, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NVARCHAR', index=16, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT', index=17, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE', index=18, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME', index=19, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEZ', index=20, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=21, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMPZ', index=22, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERVAL', index=23, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIT', index=24, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARBIT', index=25, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARY', index=26, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARBINARY', index=27, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOB', index=28, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECORD', index=29, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ANY', index=30, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UDT', index=31, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROTOBUF', index=32, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INET4', index=33, number=91,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INET6', index=34, number=92,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN_ARRAY', index=35, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT1_ARRAY', index=36, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT2_ARRAY', index=37, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT4_ARRAY', index=38, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT8_ARRAY', index=39, number=105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT1_ARRAY', index=40, number=106,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT2_ARRAY', index=41, number=107,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT4_ARRAY', index=42, number=108,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UINT8_ARRAY', index=43, number=109,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT4_ARRAY', index=44, number=110,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT8_ARRAY', index=45, number=111,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMERIC_ARRAY', index=46, number=112,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAR_ARRAY', index=47, number=121,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NCHAR_ARRAY', index=48, number=122,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VARCHAR_ARRAY', index=49, number=123,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NVARCHAR_ARRAY', index=50, number=124,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_ARRAY', index=51, number=125,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_ARRAY', index=52, number=131,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_ARRAY', index=53, number=132,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEZ_ARRAY', index=54, number=133,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP_ARRAY', index=55, number=134,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMPZ_ARRAY', index=56, number=135,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERVAL_ARRAY', index=57, number=136,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=110,
  serialized_end=935,
)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
NULL_TYPE = 0
BOOLEAN = 1
INT1 = 2
INT2 = 3
INT4 = 4
INT8 = 5
UINT1 = 6
UINT2 = 7
UINT4 = 8
UINT8 = 9
FLOAT4 = 10
FLOAT8 = 11
NUMERIC = 12
CHAR = 21
NCHAR = 22
VARCHAR = 23
NVARCHAR = 24
TEXT = 25
DATE = 31
TIME = 32
TIMEZ = 33
TIMESTAMP = 34
TIMESTAMPZ = 35
INTERVAL = 36
BIT = 41
VARBIT = 42
BINARY = 43
VARBINARY = 44
BLOB = 45
RECORD = 51
ANY = 61
UDT = 62
PROTOBUF = 63
INET4 = 91
INET6 = 92
BOOLEAN_ARRAY = 101
INT1_ARRAY = 102
INT2_ARRAY = 103
INT4_ARRAY = 104
INT8_ARRAY = 105
UINT1_ARRAY = 106
UINT2_ARRAY = 107
UINT4_ARRAY = 108
UINT8_ARRAY = 109
FLOAT4_ARRAY = 110
FLOAT8_ARRAY = 111
NUMERIC_ARRAY = 112
CHAR_ARRAY = 121
NCHAR_ARRAY = 122
VARCHAR_ARRAY = 123
NVARCHAR_ARRAY = 124
TEXT_ARRAY = 125
DATE_ARRAY = 131
TIME_ARRAY = 132
TIMEZ_ARRAY = 133
TIMESTAMP_ARRAY = 134
TIMESTAMPZ_ARRAY = 135
INTERVAL_ARRAY = 136



_DATATYPE = _descriptor.Descriptor(
  name='DataType',
  full_name='DataType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DataType.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='DataType.length', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='DataType.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_nested_fields', full_name='DataType.num_nested_fields', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  extension_ranges=[],
  serialized_start=19,
  serialized_end=107,
)

_DATATYPE.fields_by_name['type'].enum_type = _TYPE
DESCRIPTOR.message_types_by_name['DataType'] = _DATATYPE

class DataType(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DATATYPE

  # @@protoc_insertion_point(class_scope:DataType)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\026org.apache.tajo.commonB\rTajoDataTypesH\001\210\001\000\240\001\001')
import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
# @@protoc_insertion_point(module_scope)
