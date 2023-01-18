from utils.file_utils import get_devices, save_devices_async
from utils.async_wrapper import threaded_task
from models.serial_model import post_job, serial
import services.serial_services as serial_services

trackers = []

def _reset_trackers():
    global trackers
    trackers = []

def load_trackers(callback):
    global trackers
    _reset_trackers()
    def threaded_func():
        trackers = get_devices()
        callback(trackers)
    threaded_task(threaded_func, ())

def ping_tracker(tracker):
    post_job(serial_services.ping_tracker, (tracker.id, serial))