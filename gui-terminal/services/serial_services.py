from models.serial import SerialCommunicator
import models.serial_model as sm
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
    try:
        command = "5;;;"
        response = _get_res(command, serial_wait_time_medium, serial)
        if response:
            print(response)
            if response['option'] == "1":
                sm.post_job(get_registration, (serial))
            elif response['option'] == "2":
                sm.post_job(stop_call_received, (response['data'], response['sign']))
    except Exception as e:
        print(e)

def get_registration(serial: SerialCommunicator):
    command = "110;;;"
    response = _get_res(command, serial_wait_time_medium, serial)
    if response:
        # decide to register it or not
        pass

def stop_call_received(address: str, signature: str):
    pass

def start_call(serial: SerialCommunicator, address: str):
    try:
        computeSignature = ""
        command = "210;;{};{}".format(address, computeSignature)
        response = _get_res(command, serial_wait_time_medium, serial)
        if response:
            if response['data'] == "OK":
                # callback
                pass
            else:
                # callback
                pass
            pass
    except Exception as e:
        print(e)
        
    

def ping_tracker(serial: SerialCommunicator, id: int):
    try:
        command = "200;;{};".format(id)
        response = _get_res(command, serial_wait_time_medium, serial)
        if response:
            if response['data'] == "OK":
                print(response)
                pass
            else:
                print(response)
                pass
            pass
    except Exception as e:
        print(e)
