import proto.CatalogProtos_pb2 as Catalog
import proto.DataTypes_pb2 as DataTypes

class Schema(object):
    """Table or Row Schema representation"""

    fields = []

    def __init__(self):
        """ """

    def __repr__(self):
        return repr(self.fields)

    @staticmethod
    def convert_from_proto(proto):
        fields = []
        for index, item in enumerate(proto.fields):
            # print index
            # print item.name
            # print DataTypes.Type.Name(item.dataType.type)
            col = Column(item.name)
            fields.append(col)
            s = Schema()
            s.fields = fields

        return s

class Column(object):
    """Column implementation"""
    def __init__(self, name):
        self.name = name
        #self.data_type = data_type

    def __repr__(self):
        return self.name

class DataFrame(object):
    name = ""
    uri = ""

    def __init__(self, name, uri, schema):
        self.name = name      # table name
        self.uri = uri        # table uri
        self.schema = schema  # schema


    @staticmethod
    def convert_from_tabledesc(table):
        """Convert table desc to DataFrame"""
        return DataFrame(table.table_name,
                         table.path,
                         Schema.convert_from_proto(table.schema))

    @staticmethod
    def convert_from_instanttable(table):
        """Convert table desc to DataFrame"""

    def schema(self):
        self.schema

    def print_schema(self):
        print "a"