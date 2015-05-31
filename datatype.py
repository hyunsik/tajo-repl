import json;

__all__ = {
  "NULL_TYPE", "BOOLEAN", "INT1", "INT2", "INT4", "INT8", "FLOAT4", "FLOAT8", "TIME", "DATE", "TIMESTAMP", "TEXT"
}


class DataType(object):

  @classmethod
  def type_name(cls):
    return cls.__name__[:-4].lower();

  def simpleString(self):
    return self.type_name()

  def jsonValue(self):
    return self.type_name()

  def json(self):
    return json.dumps(self.jsonValue(),
                     separators=(',', ':'),
                     sort_keys=True)


class DataTypeSingleton(type):
  """Metaclass for DataType"""

  _instances = {}

  def __call__(cls):
    if cls not in cls._instances:
      cls._instances[cls] = super(DataTypeSingleton, cls).__call__()
    return cls._instances[cls]

class Int1Type(DataType):
  """Time data type
  """

class Int2Type(DataType):
  """Time data type
  """

class Int4Type(DataType):
  """Time data type
  """

class Float4Type(DataType):
  """Time data type
  """

class Float8Type(DataType):
  """Time data type
  """

class TimeType(DataType):
  """Time data type
  """

class DateType(DataType):
  """Time data type
  """

class TimestampType(DataType):
  """Timestamp data type
  """

class TextType(DataType):
  """Time data type
  """


c= TimestampType()
print c.type_name()
print c.simpleString()
print c.jsonValue()
print c.json()
