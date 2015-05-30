from proto import TajoIdProtos_pb2
from proto import PrimitiveProtos_pb2
from proto import TajoMasterClientProtocol_pb2 as client
from proto import ClientProtos_pb2

import rlcompleter, readline
readline.parse_and_bind('tab:complete')

class TajoContext:
    host = ""
    port = 0
    sessionId = ""

    def __init__(self, host="localhost", port=28002):
        self.host = host
        self.port = port
        self.__update_session()


    def __update_session(self):
        _TIMEOUT_SECONDS = 10
        request = ClientProtos_pb2.CreateSessionRequest(username="hyunsik", baseDatabaseName="default")
        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            session = stub.createSession(request, _TIMEOUT_SECONDS)
            self.sessionId = session.sessionId.id;


    def session_id(self):
        return self.sessionId
