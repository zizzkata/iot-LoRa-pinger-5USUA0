from models.serial import SerialCommunicator
from threading import Thread, Lock
import services.serial_services as services
from config import enable_daemon, serial_port, serial_baudrate, status_request_interval
import time

daemon_sleep_time = 0.5
lock = Lock()
serial = None
running = True

jobs = []

def kill_deamon():
    global running
    running = False

def post_job(target, args):
    global jobs, lock, serial
    if serial:
        lock.acquire()
        jobs.append((target, args))
        lock.release()
    else:
        print("Serial not connected")

def run_job(serial: SerialCommunicator):
    global jobs, lock
    lock.acquire()
    job_run = False
    if len(jobs) > 0:
        (target, args) = jobs.pop(0)
        target(*args)
    lock.release()
    return job_run
    
def serial_daemon():
    global serial, jobs, lock, running
    if not enable_daemon:
        return
    print("Serial daemon started")
    last_time_status_sent = time.time()
    try:
        serial = SerialCommunicator(serial_port, serial_baudrate)
    except Exception as e:
        print("Failed to connect to serial port")
        print(e)
    if serial:
        while running:
            if (time.time() - last_time_status_sent) > status_request_interval:
                # post_job(services.get_status, (serial,))
                post_job(services.ping_tracker, (serial,1,))
                last_time_status_sent = time.time()
            run_job(serial)
            time.sleep(daemon_sleep_time)
        print("Serial daemon stopped")

serialThread = Thread(target=serial_daemon, args=())
serialThread.daemon = True

def start_serial_daemon():
    global serialThread
    serialThread.start()