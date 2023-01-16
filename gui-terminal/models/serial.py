from serial import *

class SerialCommunicator(Serial):
    def __init__(self, port, baudrate, timeout=1, **kwargs):
        super(SerialCommunicator, self).__init__(port, baudrate, timeout, **kwargs)
        self.open()
    
    def send(self, data: str):
        self.readline()
        self.write(bytes(data, 'utf-8'))
    
    def receive(self):
        return self.readline().decode('utf-8').trim()