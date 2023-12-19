import serial.tools.list_ports as p
import serial
import signal
import sys
import time
##### KOMENDY STANDARD SCPI
#########################################################
'''wylistowanie dostępnych portów COM'''
ports = p.comports()
for i in ports:
    print(i)
#########################################################
'''
Funkcja przyjmuje przekonwetowany do zwykłej klasy byte string zamienionym bitem \xae na .
#ypisuje to co dostała a następnie filtruje . oraz cyfry od innych znaków.
Wynika to zaobserwowania cyfr znajdujących się na ekranie pomiędzy wszystkimi wysłanymi bitami


'''

def filtercorrupted(bytes:str):
        value = ""
        #print(bytes)
        for i in bytes:
            if i.isdigit() or i=='.':
                value += i
        return float(value)
##########################################################
Lakeshore330 = serial.Serial("COM1",1200,timeout=1,parity=serial.PARITY_NONE) # otworzenie komunikacji z lakeshorem
Lakeshore330.write(bytes("CCHN A",'ascii')) #ustawienie sondy z której wykonywany jest odczyt)
while True:
    Lakeshore330.write(b'CDAT?') #wysłanie do kontrolera zapytanie o obecną temperaturę
    a = Lakeshore330.readline()[1:7] # odczytanie odpowiedzi na wsyłane zapytanie. Nawias [1:7]
    #odpowiada za wybranie z lini bitów tych na których zapisana jest odczytana wartość
    '''sposób kodowania bitów przez lakeshore opisany w instrukcji
        |parity bit| +7*|data bit| + |parity bit| + |EOL bit|
        Uwaga w instrukcji jest napisane że pisze, że parametr parity = ODD jednak oddczytanie jakiejkowleik wiadomości
        po ustawieniu w tym programie parametru parity na odd okazała się niemożliwa
    '''
    print(filtercorrupted(str(a).replace('\\xae', '.')))