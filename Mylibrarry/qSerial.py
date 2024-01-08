import serial
import serial.tools.list_ports
STOPBITS_ONE = serial.STOPBITS_ONE
STOPBITS_ONE_POINT_FIVE = serial.STOPBITS_ONE_POINT_FIVE
STOPBITS_TWO = serial.STOPBITS_TWO
PARITY_NONE = serial.PARITY_NONE
PARITY_EVEN = serial.PARITY_EVEN
PARITY_ODD = serial.PARITY_ODD
SEVENBITS = serial.SEVENBITS
EIGHTBITS = serial.EIGHTBITS
class qSerial(serial.Serial):
    def query(self,command:str,encoding = "utf-8"):
        self.write(bytes(command,encoding))
        return self.readline().decode()
"""def __init__: definiuje inicjalizator klasy tu nie potrzebne ale tak na przyszłość"""
def available():
    answ = []
    ports = serial.tools.list_ports.comports()
    for i in ports:
        answ.append(i)
    return answ