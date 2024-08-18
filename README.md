# iot_device_management
# IoT_Devices_Management

This project is an IoT Device Management system that uses gRPC services to manage and monitor IoT devices, such as PCs and Raspberry Pi boards, within a corporate network.

## Features

### Initial Configuration Service
- **RegisterDevice**: Registers a new device with details like serial number, name, type, location, owner, and OS type.
- **UpdateOwnDevice**: Updates the details of an already registered device.
- **GetDeviceIdByDeviceName**: Retrieves the device ID using the device name.
- **ConfigureNetwork**: Configures the network settings of the device (SSID, WiFi password, IP address).

### System Status Service
- **GetSystemStatus**: Retrieves the current system status, including CPU usage, memory usage, and disk space.
- **GetLastRecord**: Fetches the last recorded system status for a device.

### Firmware Configuration Service
- **GetCurrentFirmwareVersion**: Retrieves the current firmware version installed on the device.
- **UpdateFirmware**: Updates the device's firmware to the latest version.
- **SetFirmwareVersion**: Sets the firmware version in the database after an update.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/manarHM17/IoT_Devices_Management.git
    cd IoT_Devices_Management
    ```

2. Install dependencies and set up the virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the gRPC server:
    ```bash
    python server.py
    ```

4. Test the services using a gRPC client.

