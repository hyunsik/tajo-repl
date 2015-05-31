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

import getpass

from proto import TajoIdProtos_pb2
from proto import PrimitiveProtos_pb2
from proto import TajoMasterClientProtocol_pb2 as client
from proto import ClientProtos_pb2

from dataframe import DataFrame

# for auto completion
import rlcompleter, readline

readline.parse_and_bind('tab:complete')


class TajoContext:
    host = ""
    port = 0

    username = ""
    sessionId = ""

    TIMEOUT_SECONDS = 3


    def __init__(self, host="localhost", port=28002):
        self.host = host
        self.port = port

        self.username = getpass.getuser()
        self.__update_session__()


    def __update_session__(self):
        request = ClientProtos_pb2.CreateSessionRequest(username=self.username, baseDatabaseName="default")

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            session = stub.createSession(request, self.TIMEOUT_SECONDS)
            self.sessionId = session.sessionId.id;


    def session_id(self): return self.sessionId

    def session_var(self, name):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.SessionedStringProto(sessionId = sessionId, value=name)

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.getSessionVariable(request, self.TIMEOUT_SECONDS)
            return res.value

    def user(self):
        return self.session_var("USERNAME")

    def current_tz(self):
        return self.session_var("TIMEZONE")

    def current_db(self):
        return self.session_var("CURRENT_DATABASE")


    def ls_dbs(self):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.getAllDatabases(sessionId, self.TIMEOUT_SECONDS)
            return res.values


    def ch_db(self, db_name):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.SessionedStringProto(sessionId = sessionId, value=db_name)

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.selectDatabase(request, self.TIMEOUT_SECONDS)
            return res.value

    def exist_db(self, db_name):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.SessionedStringProto(sessionId = sessionId, value=db_name)

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.existDatabase(request, self.TIMEOUT_SECONDS)
            return res.value


    def ls_tables(self, db_name=None):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.GetTableListRequest(sessionId = sessionId)

        if db_name != None:
            request.databaseName = db_name

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.getTableList(request, self.TIMEOUT_SECONDS)
            return res.tables


    def running_jobs(self):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.GetQueryListRequest(sessionId = sessionId)

        query_Ids = []
        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.getRunningQueryList(request, self.TIMEOUT_SECONDS)

            for index, item in enumerate(res.queryList):
                query_Ids.append(item.queryId)

            return query_Ids


    @staticmethod
    def __convert_query_id__(queryid):
        return 'q_' + queryid.id + '_{}'.format(queryid.seq)

    def finished_jobs(self):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.GetQueryListRequest(sessionId = sessionId)

        query_Ids = []
        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.getFinishedQueryList(request, self.TIMEOUT_SECONDS)

            for index, item in enumerate(res.queryList):
                query_Ids.append(TajoContext.__convert_query_id__(item.queryId))

            return query_Ids


    def from_table(self, name):
        sessionId = TajoIdProtos_pb2.SessionIdProto(id=self.sessionId)
        request = ClientProtos_pb2.GetTableDescRequest(sessionId=sessionId, tableName=name)

        with client.early_adopter_create_TajoMasterClientProtocolService_stub(self.host, self.port) as stub:
            res = stub.getTableDesc(request, self.TIMEOUT_SECONDS)
            return DataFrame.convert_from_tabledesc(res.tableDesc)


# c = TajoContext();
# print c.sessionId
# print c.current_db()
# lineitem = c.from_table("lineitem")
# print lineitem.name
# print lineitem.uri
#
# print lineitem.schema.fields
