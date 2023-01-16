from models.serial import SerialCommunicator
from threading import Thread, Lock
from config import enable_daemon, serial_port, serial_baudrate, status_request_interval
import time

daemon_sleep_time = 0.5
lock = Lock()

jobs = []

def post_job(target, args):
    global jobs, lock
    lock.acquire()
    jobs.append((target, args))
    lock.release()

def run_job(serial: SerialCommunicator):
    global jobs, lock
    lock.acquire()
    job_run = False
    if len(jobs) > 0:
        (target, args) = jobs.pop(0)
        # do smt    
    lock.release()
    return job_run
    
def serial_daemon():
    global jobs, lock
    print("Serial daemon started")
    last_time_status_sent = time.time()
    serial = SerialCommunicator(serial_port, serial_baudrate)
    while True:
        if (time.time() - last_time_status_sent) > status_request_interval:
            post_job(serial.send, ("status",))
            last_time_status_sent = time.time()
        run_job(serial)
        time.sleep(daemon_sleep_time)

serialThread = Thread(target=serial_daemon, args=())
serialThread.daemon = True

if enable_daemon:
    serialThread.start()