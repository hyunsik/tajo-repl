# Copyright 2015 Hyunsik Choi (hyunsik.choi@gmail.com) All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from proto import TajoIdProtos_pb2
from proto import PrimitiveProtos_pb2
from proto import TajoMasterClientProtocol_pb2 as client
from proto import ClientProtos_pb2

# for auto completion
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
