import models.serial_comm as sc
from workers.serial_reader import SerialReader
from config.constants import DB_NAME


if __name__ == '__main__':
    if not DB_NAME.exists():
        print('The database does not exist. Create it first.')
        exit(1)
    serial_reader = SerialReader()
    workers = [serial_reader]

    for w in workers:
        w.start()
    try:
        for w in workers:
            w.join()
    except KeyboardInterrupt:
        sc.SerialComm.ser_close()
        serial_reader.close_db()
    print('Exiting...')

