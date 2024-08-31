import grpc
from concurrent import futures
import mysql.connector
from mysql.connector import Error
import device_pb2
import device_pb2_grpc

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="grpc",
            password="grpc",
            database="iot_device_management"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def setup_database_and_tables():
    connection = get_db_connection()
    if connection is None:
        print("Failed to connect to MySQL.")
        return

    cursor = connection.cursor()
    try:
        # Check if the database exists; if not, create it
        cursor.execute("SHOW DATABASES LIKE 'iot_device_management'")
        result = cursor.fetchone()
        if not result:
            cursor.execute("CREATE DATABASE iot_device_management")
            print("Database 'iot_device_management' created.")

        # Reconnect to the database
        connection.database = 'iot_device_management'

        # Create tables if they do not exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS devices (
                id INT AUTO_INCREMENT PRIMARY KEY,
                serial_number VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                type VARCHAR(255) NOT NULL,
                location VARCHAR(255),
                owner VARCHAR(255),
                os_type VARCHAR(255),
                firmware_version VARCHAR(255),
                ssid VARCHAR(255),
                wifi_password VARCHAR(255),
                ip_address VARCHAR(255)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS device_monitoring (
                id INT AUTO_INCREMENT PRIMARY KEY,
                device_id INT NOT NULL,
                cpu_usage VARCHAR(255) NOT NULL,
                memory_usage VARCHAR(255) NOT NULL,
                disk_space VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (device_id) REFERENCES devices(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS firmware (
                id INT AUTO_INCREMENT PRIMARY KEY,
                version VARCHAR(255) NOT NULL,
                device_type VARCHAR(255) NOT NULL,
                binary_file VARCHAR(255) NOT NULL,
                release_date DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

        print("Tables checked and created if necessary.")

    except Error as e:
        print(f"Error setting up database and tables: {e}")

    finally:
        cursor.close()
        connection.close()

class InitialConfiguration(device_pb2_grpc.InitialConfigurationServicer):
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()

    def RegisterDevice(self, request, context):
        sql = """
           INSERT INTO devices (serial_number, name, type, location, owner, os_type)
           VALUES (%s, %s, %s, %s, %s, %s)
           """
        values = (
            request.serial_number,
            request.name,
            request.type,
            request.location,
            request.owner,
            request.os_type
        )
        try:
            self.cursor.execute(sql, values)
            self.db_connection.commit()
            device_id = self.cursor.lastrowid
            print(f"Device registered successfully: {device_id}")
            return device_pb2.RegisterDeviceResponse(message="Device registered successfully", device_id=device_id)
        except mysql.connector.Error as err:
            context.set_details(f"Error registering device: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.RegisterDeviceResponse(message=f"Failed to register device: {err}", device_id=0)

    def DeleteDevice(self, request, context):
        device_id = request.device_id
        sql = "DELETE FROM devices WHERE id = %s"
        try:
            self.cursor.execute(sql, (device_id,))
            self.db_connection.commit()
            print(f"Device deleted successfully: {request.device_id}")
            if self.cursor.rowcount > 0:
                return device_pb2.DeleteDeviceResponse(success=True, message="Device deleted successfully")
            else:
                context.set_details("Device not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return device_pb2.DeleteDeviceResponse(success=False, message="Device not found")
        except mysql.connector.Error as err:
            context.set_details(f"Error deleting device: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.DeleteDeviceResponse(success=False, message=f"Failed to delete device: {err}")
    def UpdateOwnDevice(self, request, context):
        sql = """
           UPDATE devices
           SET name = %s, owner = %s, os_type = %s, location = %s
           WHERE id = %s
           """
        values = (
            request.name,
            request.owner,
            request.os_type,
            request.location,
            request.device_id
        )
        try:
            self.cursor.execute(sql, values)
            self.db_connection.commit()
            print(f"Device updated successfully: {request.device_id}")
            return device_pb2.UpdateOwnDeviceResponse(message="Device updated successfully")
        except mysql.connector.Error as err:
            context.set_details(f"Error updating device: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.UpdateOwnDeviceResponse(message=f"Failed to update device: {err}")

    def GetDeviceIdByDeviceName(self, request, context):
        sql = "SELECT id FROM devices WHERE name = %s"
        try:
            self.cursor.execute(sql, (request.device_name,))
            device_id = self.cursor.fetchone()
            if device_id:
                print(f"Device ID fetched successfully: {device_id[0]}")
                return device_pb2.GetDeviceIdByDeviceNameResponse(device_id=device_id[0])
            else:
                context.set_details("Device not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return device_pb2.GetDeviceIdByDeviceNameResponse(device_id=0)
        except mysql.connector.Error as err:
            context.set_details(f"Error fetching device ID: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.GetDeviceIdByDeviceNameResponse(device_id=0)

    def ConfigureNetwork(self, request, context):
        sql = """
               UPDATE devices
               SET ssid = %s, wifi_password = %s, ip_address = %s
               WHERE id = %s
           """
        values = (request.ssid, request.wifi_password, request.ip_address, request.device_id)
        try:
            self.cursor.execute(sql, values)
            self.db_connection.commit()
            print(f"Network configuration updated successfully for device ID: {request.device_id}")
            return device_pb2.ConfigureNetworkResponse(message="Network configuration updated successfully")
        except mysql.connector.Error as err:
            context.set_details(f"Error updating network configuration: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.ConfigureNetworkResponse(message=f"Failed to update network configuration: {err}")

class SystemStatusService(device_pb2_grpc.SystemStatusServiceServicer):
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()

    def GetSystemStatus(self, request, context):
        sql = """
             INSERT INTO device_monitoring (device_id, cpu_usage, memory_usage, disk_space)
             VALUES (%s, %s, %s, %s)
             """
        values = (request.device_id, request.cpu_usage, request.memory_usage, request.disk_space)
        try:
            self.cursor.execute(sql, values)
            self.db_connection.commit()
            print(f"System status recorded successfully for device ID: {request.device_id}")
            return device_pb2.SystemStatusResponse(message="System status recorded successfully")
        except mysql.connector.Error as err:
            context.set_details(f"Error recording system status: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.SystemStatusResponse(message=f"Failed to record system status: {err}")

    def GetLastRecord(self, request, context):
        sql = "SELECT cpu_usage, memory_usage, disk_space, timestamp FROM device_monitoring WHERE device_id = %s ORDER BY timestamp DESC LIMIT 1"
        try:
            self.cursor.execute(sql, (request.device_id,))
            record = self.cursor.fetchone()
            if record:
                print(f"Last record retrieved successfully for device ID: {request.device_id}")
                return device_pb2.GetLastRecordResponse(
                    cpu_usage=record[0],
                    memory_usage=record[1],
                    disk_space=record[2],
                    timestamp=str(record[3]),
                    message="Last record retrieved successfully"
                )
            else:
                context.set_details("No record found for the device")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return device_pb2.GetLastRecordResponse(message="No record found for the device")
        except mysql.connector.Error as err:
            context.set_details(f"Error retrieving last record: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.GetLastRecordResponse(message=f"Failed to retrieve last record: {err}")

class FirmwareConfigurationService(device_pb2_grpc.FirmwareConfigurationServicer):
    def __init__(self):
        self.db_connection = get_db_connection()
        self.cursor = self.db_connection.cursor()

    def GetCurrentFirmwareVersion(self, request, context):
        device_id = request.device_id
        sql = "SELECT firmware_version FROM devices WHERE id = %s"
        try:
            self.cursor.execute(sql, (device_id,))
            firmware_version = self.cursor.fetchone()
            if firmware_version:
                print(f"Current firmware version retrieved successfully for device ID: {device_id}")
                return device_pb2.FirmwareResponse(current_version=firmware_version[0])
            else:
                context.set_details("Device not found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return device_pb2.FirmwareResponse(current_version="")
        except mysql.connector.Error as err:
            context.set_details(f"Error retrieving firmware version: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.FirmwareResponse(current_version="")

    def UpdateFirmware(self, request, context):
        device_id = request.device_id
        sql_firmware = "SELECT version, binary_file FROM firmware ORDER BY release_date DESC LIMIT 1"
        try:
            self.cursor.execute(sql_firmware)
            firmware = self.cursor.fetchone()
            if firmware:
                firmware_version = firmware[0]
                binary_file_path = firmware[1]
                with open(binary_file_path, 'rb') as f:
                    binary_data = f.read()

                print(f"Firmware update available: Version {firmware_version}")
                return device_pb2.UpdateFirmwareResponse(
                    success=True,
                    message="Firmware update available.",
                    firmware_version=firmware_version,
                    firmware_binary_data=binary_data
                )
            else:
                context.set_details("No firmware found")
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return device_pb2.UpdateFirmwareResponse(
                    success=False,
                    message="No firmware found",
                    firmware_version=""
                )
        except mysql.connector.Error as err:
            context.set_details(f"Error updating firmware: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.UpdateFirmwareResponse(
                success=False,
                message=f"Failed to update firmware: {err}",
                firmware_version=""
            )

    def SetFirmwareVersion(self, request, context):
        device_id = request.device_id
        firmware_version = request.firmware_version  # Use firmware_version as defined in .proto

        sql = "UPDATE devices SET firmware_version = %s WHERE id = %s"
        try:
            self.cursor.execute(sql, (firmware_version, device_id))
            self.db_connection.commit()
            print(f"Firmware version updated successfully for device ID: {device_id}")
            return device_pb2.SetFirmwareVersionResponse(
                success=True,
                message="Firmware version updated successfully."
            )
        except mysql.connector.Error as err:
            context.set_details(f"Error setting firmware version: {err}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return device_pb2.SetFirmwareVersionResponse(
                success=False,
                message=f"Failed to set firmware version: {err}"
            )
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    device_pb2_grpc.add_InitialConfigurationServicer_to_server(InitialConfiguration(), server)
    device_pb2_grpc.add_SystemStatusServiceServicer_to_server(SystemStatusService(), server)
    device_pb2_grpc.add_FirmwareConfigurationServicer_to_server(FirmwareConfigurationService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    setup_database_and_tables()
    serve()
