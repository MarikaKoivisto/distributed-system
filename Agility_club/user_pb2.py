# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"9\n\x13RegisterUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\'\n\x14RegisterUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"=\n\x17\x41uthenticateUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"<\n\x18\x41uthenticateUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\"\n\x0eGetUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\"A\n\x0fGetUserResponse\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\r\n\x05roles\x18\x03 \x03(\t\"1\n\x0bUserRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1f\n\x0cUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x9f\x02\n\x04User\x12G\n\x0cRegisterUser\x12\x19.user.RegisterUserRequest\x1a\x1a.user.RegisterUserResponse\"\x00\x12S\n\x10\x41uthenticateUser\x12\x1d.user.AuthenticateUserRequest\x1a\x1e.user.AuthenticateUserResponse\"\x00\x12\x38\n\x07GetUser\x12\x14.user.GetUserRequest\x1a\x15.user.GetUserResponse\"\x00\x12?\n\x14\x43heckUserCredentials\x12\x11.user.UserRequest\x1a\x12.user.UserResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERUSERREQUEST._serialized_start=20
  _REGISTERUSERREQUEST._serialized_end=77
  _REGISTERUSERRESPONSE._serialized_start=79
  _REGISTERUSERRESPONSE._serialized_end=118
  _AUTHENTICATEUSERREQUEST._serialized_start=120
  _AUTHENTICATEUSERREQUEST._serialized_end=181
  _AUTHENTICATEUSERRESPONSE._serialized_start=183
  _AUTHENTICATEUSERRESPONSE._serialized_end=243
  _GETUSERREQUEST._serialized_start=245
  _GETUSERREQUEST._serialized_end=279
  _GETUSERRESPONSE._serialized_start=281
  _GETUSERRESPONSE._serialized_end=346
  _USERREQUEST._serialized_start=348
  _USERREQUEST._serialized_end=397
  _USERRESPONSE._serialized_start=399
  _USERRESPONSE._serialized_end=430
  _USER._serialized_start=433
  _USER._serialized_end=720
# @@protoc_insertion_point(module_scope)
