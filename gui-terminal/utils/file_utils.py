from config import users_file_path, devices_file_path
from utils.async_wrapper import *
import json

def get_user():
    with open(users_file_path, "r") as f:
        return json.load(f)

def get_devices():
    with open(devices_file_path, "r") as f:
        return json.load(f)

def _save_user(user):
    with open(users_file_path, "w") as f:
        json.dump(user, f)

def _save_devices(devices):
    with open(devices_file_path, "w") as f:
        json.dump(devices, f)

def save_user_async(user):
    threaded_task(_save_user, (user,))

def save_devices_async(devices):
    threaded_task(_save_devices, (devices,))