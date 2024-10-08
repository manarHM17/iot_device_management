# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x64\x65vice.proto\x12\x14IotDeviceManagement2\"|\n\x15RegisterDeviceRequest\x12\x15\n\rserial_number\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\r\n\x05owner\x18\x05 \x01(\t\x12\x0f\n\x07os_type\x18\x06 \x01(\t\"<\n\x16RegisterDeviceResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\x05\"k\n\x16UpdateOwnDeviceRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x0f\n\x07os_type\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\"*\n\x17UpdateOwnDeviceResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"5\n\x1eGetDeviceIdByDeviceNameRequest\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\"4\n\x1fGetDeviceIdByDeviceNameResponse\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\"e\n\x17\x43onfigureNetworkRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\x12\x0c\n\x04ssid\x18\x02 \x01(\t\x12\x15\n\rwifi_password\x18\x03 \x01(\t\x12\x12\n\nip_address\x18\x04 \x01(\t\"+\n\x18\x43onfigureNetworkResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"e\n\x13SystemStatusRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\x12\x11\n\tcpu_usage\x18\x02 \x01(\t\x12\x14\n\x0cmemory_usage\x18\x03 \x01(\t\x12\x12\n\ndisk_space\x18\x04 \x01(\t\"\'\n\x14SystemStatusResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x14GetLastRecordRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\"x\n\x15GetLastRecordResponse\x12\x11\n\tcpu_usage\x18\x01 \x01(\t\x12\x14\n\x0cmemory_usage\x18\x02 \x01(\t\x12\x12\n\ndisk_space\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x0f\n\x07message\x18\x05 \x01(\t\"$\n\x0f\x46irmwareRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\"+\n\x10\x46irmwareResponse\x12\x17\n\x0f\x63urrent_version\x18\x01 \x01(\t\"*\n\x15UpdateFirmwareRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\"r\n\x16UpdateFirmwareResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x10\x66irmware_version\x18\x03 \x01(\t\x12\x1c\n\x14\x66irmware_binary_data\x18\x04 \x01(\x0c\"H\n\x19SetFirmwareVersionRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\x12\x18\n\x10\x66irmware_version\x18\x02 \x01(\t\">\n\x1aSetFirmwareVersionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"(\n\x13\x44\x65leteDeviceRequest\x12\x11\n\tdevice_id\x18\x01 \x01(\x05\"8\n\x14\x44\x65leteDeviceResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xd6\x04\n\x14InitialConfiguration\x12k\n\x0eRegisterDevice\x12+.IotDeviceManagement2.RegisterDeviceRequest\x1a,.IotDeviceManagement2.RegisterDeviceResponse\x12n\n\x0fUpdateOwnDevice\x12,.IotDeviceManagement2.UpdateOwnDeviceRequest\x1a-.IotDeviceManagement2.UpdateOwnDeviceResponse\x12\x86\x01\n\x17GetDeviceIdByDeviceName\x12\x34.IotDeviceManagement2.GetDeviceIdByDeviceNameRequest\x1a\x35.IotDeviceManagement2.GetDeviceIdByDeviceNameResponse\x12q\n\x10\x43onfigureNetwork\x12-.IotDeviceManagement2.ConfigureNetworkRequest\x1a..IotDeviceManagement2.ConfigureNetworkResponse\x12\x65\n\x0c\x44\x65leteDevice\x12).IotDeviceManagement2.DeleteDeviceRequest\x1a*.IotDeviceManagement2.DeleteDeviceResponse2\xe9\x01\n\x13SystemStatusService\x12h\n\x0fGetSystemStatus\x12).IotDeviceManagement2.SystemStatusRequest\x1a*.IotDeviceManagement2.SystemStatusResponse\x12h\n\rGetLastRecord\x12*.IotDeviceManagement2.GetLastRecordRequest\x1a+.IotDeviceManagement2.GetLastRecordResponse2\xe9\x02\n\x15\x46irmwareConfiguration\x12j\n\x19GetCurrentFirmwareVersion\x12%.IotDeviceManagement2.FirmwareRequest\x1a&.IotDeviceManagement2.FirmwareResponse\x12k\n\x0eUpdateFirmware\x12+.IotDeviceManagement2.UpdateFirmwareRequest\x1a,.IotDeviceManagement2.UpdateFirmwareResponse\x12w\n\x12SetFirmwareVersion\x12/.IotDeviceManagement2.SetFirmwareVersionRequest\x1a\x30.IotDeviceManagement2.SetFirmwareVersionResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'device_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGISTERDEVICEREQUEST']._serialized_start=38
  _globals['_REGISTERDEVICEREQUEST']._serialized_end=162
  _globals['_REGISTERDEVICERESPONSE']._serialized_start=164
  _globals['_REGISTERDEVICERESPONSE']._serialized_end=224
  _globals['_UPDATEOWNDEVICEREQUEST']._serialized_start=226
  _globals['_UPDATEOWNDEVICEREQUEST']._serialized_end=333
  _globals['_UPDATEOWNDEVICERESPONSE']._serialized_start=335
  _globals['_UPDATEOWNDEVICERESPONSE']._serialized_end=377
  _globals['_GETDEVICEIDBYDEVICENAMEREQUEST']._serialized_start=379
  _globals['_GETDEVICEIDBYDEVICENAMEREQUEST']._serialized_end=432
  _globals['_GETDEVICEIDBYDEVICENAMERESPONSE']._serialized_start=434
  _globals['_GETDEVICEIDBYDEVICENAMERESPONSE']._serialized_end=486
  _globals['_CONFIGURENETWORKREQUEST']._serialized_start=488
  _globals['_CONFIGURENETWORKREQUEST']._serialized_end=589
  _globals['_CONFIGURENETWORKRESPONSE']._serialized_start=591
  _globals['_CONFIGURENETWORKRESPONSE']._serialized_end=634
  _globals['_SYSTEMSTATUSREQUEST']._serialized_start=636
  _globals['_SYSTEMSTATUSREQUEST']._serialized_end=737
  _globals['_SYSTEMSTATUSRESPONSE']._serialized_start=739
  _globals['_SYSTEMSTATUSRESPONSE']._serialized_end=778
  _globals['_GETLASTRECORDREQUEST']._serialized_start=780
  _globals['_GETLASTRECORDREQUEST']._serialized_end=821
  _globals['_GETLASTRECORDRESPONSE']._serialized_start=823
  _globals['_GETLASTRECORDRESPONSE']._serialized_end=943
  _globals['_FIRMWAREREQUEST']._serialized_start=945
  _globals['_FIRMWAREREQUEST']._serialized_end=981
  _globals['_FIRMWARERESPONSE']._serialized_start=983
  _globals['_FIRMWARERESPONSE']._serialized_end=1026
  _globals['_UPDATEFIRMWAREREQUEST']._serialized_start=1028
  _globals['_UPDATEFIRMWAREREQUEST']._serialized_end=1070
  _globals['_UPDATEFIRMWARERESPONSE']._serialized_start=1072
  _globals['_UPDATEFIRMWARERESPONSE']._serialized_end=1186
  _globals['_SETFIRMWAREVERSIONREQUEST']._serialized_start=1188
  _globals['_SETFIRMWAREVERSIONREQUEST']._serialized_end=1260
  _globals['_SETFIRMWAREVERSIONRESPONSE']._serialized_start=1262
  _globals['_SETFIRMWAREVERSIONRESPONSE']._serialized_end=1324
  _globals['_DELETEDEVICEREQUEST']._serialized_start=1326
  _globals['_DELETEDEVICEREQUEST']._serialized_end=1366
  _globals['_DELETEDEVICERESPONSE']._serialized_start=1368
  _globals['_DELETEDEVICERESPONSE']._serialized_end=1424
  _globals['_INITIALCONFIGURATION']._serialized_start=1427
  _globals['_INITIALCONFIGURATION']._serialized_end=2025
  _globals['_SYSTEMSTATUSSERVICE']._serialized_start=2028
  _globals['_SYSTEMSTATUSSERVICE']._serialized_end=2261
  _globals['_FIRMWARECONFIGURATION']._serialized_start=2264
  _globals['_FIRMWARECONFIGURATION']._serialized_end=2625
# @@protoc_insertion_point(module_scope)
