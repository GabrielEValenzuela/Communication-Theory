import sqlite3
import datetime as dt
import random
from config.constants import VALID_NODES, DB_NAME

MAX_TEMP = 41.5
MIN_TEMP = 1.3

if __name__ == '__main__':
    conn = sqlite3.connect(str(DB_NAME))
    cursor = conn.cursor()
    node_records = []
    for key, value in VALID_NODES.items():
        node_records.append((key, value))
    try:
        cursor.executemany('''INSERT INTO nodes (node_number, node_name)
                VALUES (?, ?)
                 ''', node_records)
    except sqlite3.DatabaseError as e:
        print('error en comando: {}'.format(e))
    cursor.execute('''SELECT * FROM nodes
    ;''')
    print(cursor.fetchall())
    conn.close()
