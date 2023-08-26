from socket import *

server_port = int(input('Enter server port number: '))

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))

server_socket.listen(1) # listen for one process from client
                        # connecting to 'special welcoming socket'
print('[+] The server is ready.')
while True:
    connect_socket, addr = server_socket.accept()
    sentence = connect_socket.recv(2048).decode()
    capitalized_sentence = sentence.upper()
    connect_socket.send(capitalized_sentence.encode())
    connect_socket.close()