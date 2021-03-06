# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QueryMasterClientProtocol.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tajo_protos_pb2
import TajoIdProtos_pb2
import CatalogProtos_pb2
import PrimitiveProtos_pb2
import ClientProtos_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='QueryMasterClientProtocol.proto',
  package='',
  serialized_pb='\n\x1fQueryMasterClientProtocol.proto\x1a\x11tajo_protos.proto\x1a\x12TajoIdProtos.proto\x1a\x13\x43\x61talogProtos.proto\x1a\x15PrimitiveProtos.proto\x1a\x12\x43lientProtos.proto2`\n QueryMasterClientProtocolService\x12<\n\x0fgetQueryHistory\x12\x0f.QueryIdRequest\x1a\x18.GetQueryHistoryResponseB6\n\x13org.apache.tajo.ipcB\x19QueryMasterClientProtocol\x88\x01\x01\xa0\x01\x01')





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\023org.apache.tajo.ipcB\031QueryMasterClientProtocol\210\001\001\240\001\001')
import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
class EarlyAdopterQueryMasterClientProtocolServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def getQueryHistory(self, request, context):
    raise NotImplementedError()
class EarlyAdopterQueryMasterClientProtocolServiceServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterQueryMasterClientProtocolServiceStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def getQueryHistory(self, request):
    raise NotImplementedError()
  getQueryHistory.async = None
def early_adopter_create_QueryMasterClientProtocolService_server(servicer, port, private_key=None, certificate_chain=None):
  import ClientProtos_pb2
  import ClientProtos_pb2
  method_service_descriptions = {
    "getQueryHistory": utilities.unary_unary_service_description(
      servicer.getQueryHistory,
      ClientProtos_pb2.QueryIdRequest.FromString,
      ClientProtos_pb2.GetQueryHistoryResponse.SerializeToString,
    ),
  }
  return implementations.server("QueryMasterClientProtocolService", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_QueryMasterClientProtocolService_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import ClientProtos_pb2
  import ClientProtos_pb2
  method_invocation_descriptions = {
    "getQueryHistory": utilities.unary_unary_invocation_description(
      ClientProtos_pb2.QueryIdRequest.SerializeToString,
      ClientProtos_pb2.GetQueryHistoryResponse.FromString,
    ),
  }
  return implementations.stub("QueryMasterClientProtocolService", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)
# @@protoc_insertion_point(module_scope)
