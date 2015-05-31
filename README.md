# Repl for Apache Tajo

This is a read–eval–print loop (repl) implementation for Apache Tajo. 
It is implmeneted in Python 2.7 and uses grpc (https://github.com/grpc/grpc) to communit Apache Tajo.

# Authors
 * Hyunsik Choi (hyunsik dot choi at gmail dot com)

# License
 * [Apache License 2.0] (http://www.apache.org/licenses/LICENSE-2.0)

# Prerequisites

* Install Apache Tajo 0.11.0-SNAPSHOT
* Install tajo-grpc-proxy (https://github.com/hyunsik/tajo-grpc-proxy)
* Install python packages (enum34, futures, protobuf)
```
pip install enum34==1.0.4
pip install futures==2.2.0
pip install protobuf==3.0.0a2
```
* Install grpcio (https://pypi.python.org/pypi/grpcio/0.9.0a0)

# Running

```sh
cd tajo-0.11.0-SNAPSHOT
bin/start-tajo.sh

cd tajo-grpc-proxy
./start-proxy.sh localhost:26002 localhost:28002

cd tajo-repl
./pytajo
```

# How to use

```
hyunsik@workstation:~/Code/tajo/tajo-repl$ ./pytajo 
Python 2.7.9 (default, Apr  2 2015, 15:33:21) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> c = TajoContext()
I0530 23:46:40.457410171    4236 socket_utils_common_posix.c:148] Disabling AF_INET6 sockets because ::1 is not available.
>>> c.session_id()
u'8b992bc2-8b54-49e5-9ceb-13563ffd35be'
>>> c.current_db()
u'default'
>>> c.list_db()
[u'default', u'information_schema']
>>> lineitem = c.from_table("lineitem")
>>> lineitem.name
u'default.lineitem'
>>> lineitem.schema
[default.lineitem.l_orderkey, default.lineitem.l_partkey, default.lineitem.l_suppkey, default.lineitem.l_linenumber, default.lineitem.l_quantity, default.lineitem.l_extendedprice, default.lineitem.l_discount, default.lineitem.l_tax, default.lineitem.l_returnflag, default.lineitem.l_linestatus, default.lineitem.l_shipdate, default.lineitem.l_commitdate, default.lineitem.l_receiptdate, default.lineitem.l_shipinstruct, default.lineitem.l_shipmode, default.lineitem.l_comment]
```


