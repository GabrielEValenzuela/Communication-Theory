import sqlite3
from config.constants import DB_NAME


if __name__ == '__main__':
    conn = sqlite3.connect(str(DB_NAME), detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nodes
    (node_number INTEGER PRIMARY KEY ,
     node_name VARCHAR(30) NOT NULL );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS temperature
    (temperature_id INTEGER PRIMARY KEY,
    temperature REAL NOT NULL,
    time_stamp TIMESTAMP,
     node_id INTEGER NOT NULL,
        FOREIGN KEY (node_id) REFERENCES nodes(node_number));''')
    conn.commit()
    conn.close()

