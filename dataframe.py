import proto.CatalogProtos_pb2 as Catalog

class Schema(object):
    """
    """
    @staticmethod
    def convert_from_proto(proto):
        print proto.fields
        return "test"

class Column(object):
    """Column implementation"""

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
        print "a"

    def print_schema(self):
        print "a"