# IoT Device Management (gRPC)

This repository contains a small example of IoT device management using gRPC and Protocol Buffers in Python. The example includes a server, a sample client, the proto definition, generated stubs, and example firmware files.


<img width="361" height="411" alt="image" src="https://github.com/user-attachments/assets/bf7a0c3e-005c-415b-a750-4d990b309028" />


## Repository contents

- server.py — gRPC server implementation (device manager).
- client.py — Example gRPC client that talks to the server (simulates a device or admin client).
- device.proto — Protocol Buffers service and messages.
- device_pb2.py, device_pb2_grpc.py — Generated Python protobuf and gRPC bindings (included for convenience).
- new_firmware_version.bin — example firmware binary placed at repository root.
- firmware_version/ — folder containing firmware images (example: rpi_firmware_1.0.0.bin).
- requirements.txt — Python dependencies used by the project.

> Note: The project layout may be minimal on purpose. Inspect `server.py` and `client.py` for implementation details such as default host/port and available RPCs.

## Goals

- Demonstrate a simple gRPC-based server that manages devices.
- Provide an example client which can request firmware or perform management operations.
- Show how to generate and use protobuf/gRPC bindings in Python.

## Prerequisites

- Python 3.8 or newer
- pip
- (optional) virtualenv or venv

Recommended Python packages (already listed in `requirements.txt`):
- grpcio
- grpcio-tools
- protobuf

Install prerequisites:

```powershell
# Create and activate a venv (Windows PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you prefer not to use the included generated stubs, generate them from the proto:

```powershell
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. device.proto
```

This creates or updates `device_pb2.py` and `device_pb2_grpc.py` in the current directory.

## Running the server and client

The exact command-line flags (port, host, TLS, etc.) depend on the implementations inside `server.py` and `client.py`. Typical usage:

```powershell
# Start the server 
python server.py

# In another shell, run the sample client
python client.py
```

If `server.py` uses a default port (for example 50051), you may need to match that in the client or provide the host/port as arguments — check the top of those files for details.

## Firmware update flow (example)

This repo includes example firmware binaries. A common flow for firmware distribution using gRPC is:

1. A device (or admin client) connects to the gRPC server and requests the available firmware version or checks the current version.
2. The server responds with metadata (version, checksum, download URL or binary stream).
3. The client downloads the binary (either via streaming RPC or by receiving a download URL the device can fetch).
4. The device verifies the firmware (checksum/signature) and applies it.

Files in this repo that illustrate the above:
- `firmware_version/rpi_firmware_1.0.0.bin` — an example firmware file.
- `new_firmware_version.bin` — another example firmware binary at repo root.

The sample `server.py` likely exposes RPCs for e.g., GetFirmwareList, GetFirmware, ReportStatus — check the proto in `device.proto` for exact method names.

## Protobuf / gRPC notes

- `device.proto` contains the service and message definitions. Use grpc_tools.protoc to generate the Python bindings as shown above if you need to regenerate them.
- The generated files are included (`device_pb2.py` and `device_pb2_grpc.py`) to make running the examples easier without installing the protoc tool.

## Development notes

- If you change `device.proto`, regenerate the Python gRPC code and re-run the server and client.
- Keep the firmware binaries out of source control for real projects; use an artifact store or signed releases instead.
- For production-grade deployments, secure the gRPC channel with TLS and add authentication/authorization for management operations.



## Where to look next

- Inspect `device.proto` to see the data model and RPC signatures.
- Open `server.py` to learn how the server handles firmware requests and device status.
- Run `client.py` to simulate device interactions.

        
