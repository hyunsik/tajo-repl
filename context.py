from proto import pkernel_client_protocol_pb2
from proto import TajoIdProtos_pb2
from proto import PrimitiveProtos_pb2

class TajoContext:
    host = ""
    port = 0

    def __init__(self, host="localhost", port="26080"):
        self.host = host
        self.port = port

    # def stop(self):
    #
    # def textFile(self, path):
    #
    # def table(self, path, format):
    #
    # def broadcast(self, value):
    #
    # def addFile(self, path):
    #
    # def addPyFile(self, path):

    def username(self):
        session_id = TajoIdProtos_pb2.SessionIdProto;
        session_id.id = "x1234567890"
        with pkernel_client_protocol_pb2.early_adopter_create_PKernelClientProtocol_stub('localhost', 20065) as stub:
            response = stub.GetUsername(session_id)
            print "Greeter client received: " + response.value
