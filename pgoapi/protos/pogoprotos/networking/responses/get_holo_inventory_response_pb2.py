# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_holo_inventory_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import inventory_delta_pb2 as pogoprotos_dot_inventory_dot_inventory__delta__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_holo_inventory_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nApogoprotos/networking/responses/get_holo_inventory_response.proto\x12\x1fpogoprotos.networking.responses\x1a*pogoprotos/inventory/inventory_delta.proto\"j\n\x18GetHoloInventoryResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12=\n\x0finventory_delta\x18\x02 \x01(\x0b\x32$.pogoprotos.inventory.InventoryDeltab\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_inventory__delta__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETHOLOINVENTORYRESPONSE = _descriptor.Descriptor(
  name='GetHoloInventoryResponse',
  full_name='pogoprotos.networking.responses.GetHoloInventoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.GetHoloInventoryResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inventory_delta', full_name='pogoprotos.networking.responses.GetHoloInventoryResponse.inventory_delta', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=252,
)

_GETHOLOINVENTORYRESPONSE.fields_by_name['inventory_delta'].message_type = pogoprotos_dot_inventory_dot_inventory__delta__pb2._INVENTORYDELTA
DESCRIPTOR.message_types_by_name['GetHoloInventoryResponse'] = _GETHOLOINVENTORYRESPONSE

GetHoloInventoryResponse = _reflection.GeneratedProtocolMessageType('GetHoloInventoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETHOLOINVENTORYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_holo_inventory_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetHoloInventoryResponse)
  ))
_sym_db.RegisterMessage(GetHoloInventoryResponse)


# @@protoc_insertion_point(module_scope)
