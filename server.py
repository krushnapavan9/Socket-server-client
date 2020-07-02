import socket, sys

'''
SIZE = 1024
EOF = b'\0'

def server_program():
    server_socket = socket.socket()
    server_socket.bind((socket.gethostname(), 5000))
    server_socket.listen(2)
    print("Waiting for clients to connect...")
    connection, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = connection.recv(SIZE)
        data = data.decode()
        print(type(data))
        if data=='q':
            break
        print(data)
    connection.close()

if __name__ == '__main__':
    server_program()
'''
server_socket = socket.socket()
server_socket.bind((socket.gethostname(),1234))
server_socket.listen(5)
connection , addr =server_socket.accept()
while True:
    data = connection.recv(100)
    data = data.decode()
    if data is not None :
        print(data)
    data = input("client > ")
    connection.send(bytes(data,'utf-8'))
connection.close()
