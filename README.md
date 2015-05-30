# Repl for Apache Tajo

This is a read–eval–print loop (repl) implementation for Apache Tajo. 
It is implmeneted in Python 2.7 and uses grpc (https://github.com/grpc/grpc) to communit Apache Tajo.

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

Python 2.7.9 (default, Apr  2 2015, 15:33:21) 
[GCC 4.9.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> c = TajoContext()
I0530 03:56:47.118761411   11658 socket_utils_common_posix.c:148] Disabling AF_INET6 sockets because ::1 is not available.
>>> 
>>> c.session_id()
u'd56cdff7-dde6-455b-9d14-1f504a45d209'
>>>
```


