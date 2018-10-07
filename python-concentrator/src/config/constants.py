import pathlib

B_RATE = 9600
PORT = '/dev/ttyACM0'
SER_TIMEOUT = 7

DB_NAME = pathlib.Path('db/teocom-pbl.db')

VALID_NODES = {"1258": "Grupo A",
               "4568": "Grupo B",
               "7898": "Grupo C"}
