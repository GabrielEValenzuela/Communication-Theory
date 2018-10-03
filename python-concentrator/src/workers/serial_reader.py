import json
import threading
import models.serial_comm as sc


class SerialReader(threading.Thread):

    def __init__(self):
        super().__init__()
        self.setDaemon(False)

    def run(self):
        while True:
            s = sc.SerialComm.ser_read_line()
            if s:
                try:
                    j = json.loads(s)
                except json.JSONDecodeError:
                    print('Error converting string to json')
                    continue
                if self.check_json(j):
                    pass
                else:
                    print('Invalid data format: {}'.format(j))

    @staticmethod
    def check_json(d: dict):
        from config.constants import VALID_NODES
        k_list = list(d.keys())
        if len(k_list) == 1:
            k = k_list[0]
            val = d[k]
            if isinstance(k, str) and isinstance(val, (int, float)):
                if k in VALID_NODES:
                    return True
                return False
            else:
                return False
        else:
            return False
