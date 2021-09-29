import socket
import datetime

host = 'localhost'
port = 123


def calculate(offset):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print('Server works')
        s.bind((host, port))
        while True:
            data, addr = s.recvfrom(1024)
            current_time = datetime.datetime.now()
            wrong_time = current_time + datetime.timedelta(0, offset)
            time = str(wrong_time)
            s.sendto(time.encode('utf-8'), addr)


if __name__ == '__main__':
    with open('./config.txt') as config:
        time_offset = int(config.read())
    calculate(time_offset)
