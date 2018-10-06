import pathlib

B_RATE = 9600
PORT = '/dev/ttyUSB0'
SER_TIMEOUT = 3

DB_NAME = pathlib.Path('../db/teocom-pbl.db')

VALID_NODES = {"1258": "Grupo A",
               "4568": "Grupo B",
               "7898": "Grupo C"}
