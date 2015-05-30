from proto import TajoIdProtos_pb2
from proto import PrimitiveProtos_pb2
from proto import TajoMasterClientProtocol_pb2 as client
from proto import ClientProtos_pb2

class TajoContext:
    host = ""
    port = 0

    def __init__(self, host="localhost", port=28002):
        self.host = host
        self.port = port

    def createSession(self):
        _TIMEOUT_SECONDS = 10
        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            session = stub.CreateSession(ClientProtos_pb2.CreateSessionRequest(username="hyunsik"), _TIMEOUT_SECONDS)


c = TajoContext()
c.createSession()