#!/bin/bash -x


if [ -z $1 ];then
  echo "usage: ./gen_proto.sh [tajo source directory]"
  exit -1
fi

PROTO_GEN_DIR=proto

if [ ! -d $PROTO_GEN_DIR ];then
  mkdir $PROTO_GEN_DIR
fi

TAJO_BASE_DIR=$1

PROTO_FILES="
$TAJO_BASE_DIR/tajo-common/src/main/proto/DataTypes.proto
$TAJO_BASE_DIR/tajo-common/src/main/proto/PrimitiveProtos.proto
$TAJO_BASE_DIR/tajo-common/src/main/proto/tajo_protos.proto
$TAJO_BASE_DIR/tajo-common/src/main/proto/TajoIdProtos.proto
$TAJO_BASE_DIR/tajo-catalog/tajo-catalog-common/src/main/proto/CatalogProtos.proto
$TAJO_BASE_DIR/tajo-client/src/main/proto/ClientProtos.proto
$TAJO_BASE_DIR/tajo-client/src/main/proto/TajoMasterClientProtocol.proto
$TAJO_BASE_DIR/tajo-client/src/main/proto/QueryMasterClientProtocol.proto
"

tmpdir=`mktemp -d`

for proto in $PROTO_FILES
do
  cp $proto $tmpdir
done

sed -i"bak" '1 i\syntax = "proto2";' $tmpdir/*.proto
rm -rf $tmpdir/*.bak

GRPC_PY_PLUGIN=`which grpc_python_plugin`
protoc --proto_path=$tmpdir --python_out=${PROTO_GEN_DIR} \
--grpc_out=${PROTO_GEN_DIR} --plugin=protoc-gen-grpc="$GRPC_PY_PLUGIN" `find $tmpdir -name "*.proto"`

rm -rf $tmpdir

touch proto/__init__.py
