import models.serial_comm as sc
from workers.serial_reader import SerialReader


if __name__ == '__main__':
    serial_reader = SerialReader()
    workers = [serial_reader]

    for w in workers:
        w.start()
    try:
        for w in workers:
            w.join()
    except KeyboardInterrupt:
        sc.SerialComm.ser_close()
    print('Exiting...')

