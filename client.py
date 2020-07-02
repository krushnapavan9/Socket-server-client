
import socket, sys
'''
SIZE = 1024
EOF = b'\0'


def client_program():

    client_socket = socket.socket()
    client_socket.connect((socket.gethostname(), 5000))
   while True:
        data = bytes(input(),'utf-8')
        client_socket.send(data)
        data = data.decode()
        print(type(data))
        if data=="q":
            break

    client_socket.close()


if __name__ == '__main__':
    client_program()
'''
client_socket = socket.socket()
client_socket.connect((socket.gethostname(),1234))
while True:
    data = input("server > ")
    client_socket.send(bytes(data,'utf-8'))
    data = client_socket.recv(100)
    data  = data.decode()
    if data is not None:
        print(data)
print(client_socket.recv(100))
client_socket.close()
