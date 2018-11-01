import sqlite3

from config.constants import VALID_NODES, DB_NAME

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
