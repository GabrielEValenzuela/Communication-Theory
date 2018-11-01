import pathlib

B_RATE = 9600
# PORT = '/dev/ttyACM0'
PORT = '/dev/ttyUSB0'
SER_TIMEOUT = 7

DB_NAME = pathlib.Path('db/teocom-pbl.db')

VALID_NODES = {
    "4854": "Computación mata electrónica",
    "1704": "Emilia4Ever",
    "1313": "Braquis-J3",
    "1234": "Electrones de Laplace",
    "1095": "Vikings PANAMA",
    "1996": "Las pociones",
    "7777": "TC2000",
    "2216": "Ca(sas+pelo)",
    "1": "Tesla",
    "69": "Zanos"
}
