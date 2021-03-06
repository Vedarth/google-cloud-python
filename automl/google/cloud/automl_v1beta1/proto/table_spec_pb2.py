# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/table_spec.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import (
    io_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_io__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/table_spec.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
    serialized_pb=_b(
        '\n2google/cloud/automl_v1beta1/proto/table_spec.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*google/cloud/automl_v1beta1/proto/io.proto"\xae\x01\n\tTableSpec\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x13time_column_spec_id\x18\x02 \x01(\t\x12\x11\n\trow_count\x18\x03 \x01(\x03\x12\x14\n\x0c\x63olumn_count\x18\x07 \x01(\x03\x12?\n\rinput_configs\x18\x05 \x03(\x0b\x32(.google.cloud.automl.v1beta1.InputConfig\x12\x0c\n\x04\x65tag\x18\x06 \x01(\tB\x84\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_io__pb2.DESCRIPTOR,
    ],
)


_TABLESPEC = _descriptor.Descriptor(
    name="TableSpec",
    full_name="google.cloud.automl.v1beta1.TableSpec",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.automl.v1beta1.TableSpec.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="time_column_spec_id",
            full_name="google.cloud.automl.v1beta1.TableSpec.time_column_spec_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="row_count",
            full_name="google.cloud.automl.v1beta1.TableSpec.row_count",
            index=2,
            number=3,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="column_count",
            full_name="google.cloud.automl.v1beta1.TableSpec.column_count",
            index=3,
            number=7,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="input_configs",
            full_name="google.cloud.automl.v1beta1.TableSpec.input_configs",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="etag",
            full_name="google.cloud.automl.v1beta1.TableSpec.etag",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=158,
    serialized_end=332,
)

_TABLESPEC.fields_by_name[
    "input_configs"
].message_type = google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_io__pb2._INPUTCONFIG
DESCRIPTOR.message_types_by_name["TableSpec"] = _TABLESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TableSpec = _reflection.GeneratedProtocolMessageType(
    "TableSpec",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLESPEC,
        __module__="google.cloud.automl_v1beta1.proto.table_spec_pb2",
        __doc__="""A specification of a relational table. The table's schema is represented
  via its child column specs. It is pre-populated as part of ImportData by
  schema inference algorithm, the version of which is a required parameter
  of ImportData InputConfig. Note: While working with a table, at times
  the schema may be inconsistent with the data in the table (e.g. string
  in a FLOAT64 column). The consistency validation is done upon creation
  of a model. Used by: \* Tables
  
  
  Attributes:
      name:
          Output only. The resource name of the table spec. Form:  ``pro
          jects/{project_id}/locations/{location_id}/datasets/{dataset_i
          d}/tableSpecs/{table_spec_id}``
      time_column_spec_id:
          column\_spec\_id of the time column. Only used if the parent
          dataset's ml\_use\_column\_spec\_id is not set. Used to split
          rows into TRAIN, VALIDATE and TEST sets such that oldest rows
          go to TRAIN set, newest to TEST, and those in between to
          VALIDATE. Required type: TIMESTAMP. If both this column and
          ml\_use\_column are not set, then ML use of all rows will be
          assigned by AutoML. NOTE: Updates of this field will instantly
          affect any other users concurrently working with the dataset.
      row_count:
          Output only. The number of rows (i.e. examples) in the table.
      column_count:
          Output only. The number of columns of the table. That is, the
          number of child ColumnSpec-s.
      input_configs:
          Output only. Input configs via which data currently residing
          in the table had been imported.
      etag:
          Used to perform consistent read-modify-write updates. If not
          set, a blind "overwrite" update happens.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TableSpec)
    ),
)
_sym_db.RegisterMessage(TableSpec)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
