import serial
import threading
from config.constants import PORT, B_RATE, SER_TIMEOUT


class SerialComm:

    __ser = serial.Serial(PORT, B_RATE, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, timeout=SER_TIMEOUT)
    r_lock = threading.RLock()

    @classmethod
    def ser_read_line(cls) -> bytes:
        """Lee una linea del puerto serial(hasta encontrar el caracter \n) y la retorna"""
        with cls.r_lock:
            s = b''
            while not s:
                try:
                    s = cls.__ser.readline()
                except serial.SerialException:
                    print('Error reading serial.')
                    return b''
            return s

    @classmethod
    def close_ser(cls):
        """Cierra el puerto serial"""
        cls.__ser.close()
