import json
import threading
import models.serial_comm as sc
import sqlite3
import datetime as dt
from config.constants import DB_NAME


class SerialReader(threading.Thread):

    def __init__(self):
        super().__init__()
        self.setDaemon(False)
        self.__conn = sqlite3.connect(str(DB_NAME), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        self.__cursor = self.__conn.cursor()

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
                    try:
                        node = list(j.keys())[0]
                        self.__cursor.execute('''INSERT INTO temperature(temperature, time_stamp, node_id)
                                            VALUES (?, ?, ?)''', (j[node], dt.datetime.now(), node))
                        self.__conn.commit()
                    except sqlite3.DatabaseError as e:
                        print('Database error: {}'.format(e))
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

    def close_db(self):
        if self.__conn:
            self.__conn.close()
