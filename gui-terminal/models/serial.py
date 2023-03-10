from serial import *

class SerialCommunicator(Serial):
    def __init__(self, port, baudrate, timeout=1, **kwargs):
        super().__init__(port=port, baudrate=baudrate, timeout=timeout, **kwargs)
    
    def send(self, data: str):
        self.write(bytes(data, 'utf-8'))
    
    def receive(self):
        return self.readline().decode('utf-8').strip()
