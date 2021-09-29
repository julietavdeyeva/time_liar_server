import socket


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'', ('localhost', 123))
        data, addr = s.recvfrom(1024)
        s.close()
        print(data.decode())
