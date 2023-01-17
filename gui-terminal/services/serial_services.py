from models.serial import SerialCommunicator
from models.serial_model import post_job
from time import sleep
from utils.serial_parser import parse_serial_output

serial_wait_time = .2
serial_wait_time_medium = .4
serial_wait_time_long = .6

def _get_res(command: str, sleep_time: float, serial: SerialCommunicator):
    serial.send(command)
    sleep(sleep_time)
    return parse_serial_output(serial.receive())

def get_status(serial: SerialCommunicator):
    command = "5;;;"
    response = _get_res(command, serial_wait_time_medium, serial)
    if response:
        if response['option'] == "1":
            post_job(get_registration, (serial))
        elif response['option'] == "2":
            post_job(stop_call_received, (response['data'], response['sign']))

def get_registration(serial: SerialCommunicator):
    command = "110;;;"
    response = _get_res(command, serial_wait_time_medium, serial)
    if response:
        # decide to register it or not
        pass

def stop_call_received(address: str, signature: str):
    pass

def start_call(serial: SerialCommunicator, address: str):
    computeSignature = ""
    command = "1;{};OK;{}".format(address, computeSignature)
    response = _get_res(command, serial_wait_time_medium, serial)
    if response:
        if response['data'] == "OK":
            # callback
            pass
        else:
            # callback
            pass
        pass
