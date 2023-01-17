import os

relative_path: str = os.path.dirname(__file__)
application_name: str = "Item Tracker"
application_size: str = "1024x600"
header_font: str = ("Bahnschrift SemiCondensed", 14)
button_font: str = ("Bahnschrift SemiCondensed", 14)

# Data paths
users_file_path: str = relative_path + "\\data\\user.json"
devices_file_path: str = relative_path + "\\data\\devices.json"
pub_key_file_path: str = relative_path + "\\data\\key.pub"
private_key_file_path: str = relative_path + "\\data\\key"

# Serial port
serial_port: str = "ttyS3"
serial_baudrate: int = 9600
enable_daemon: bool = False
status_request_interval: int = 3
