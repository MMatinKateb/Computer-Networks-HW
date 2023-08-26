from socket import *

server_name = input('Enter hostname: ')
server_port = int(input('Enter server port number: '))

client_socket = socket(AF_INET, SOCK_STREAM)        # IPv4 + TCP
client_socket.connect((server_name, server_port))   # 3-way handshake configuration

sentence = input('Enter lowercase sentence: ').encode()
client_socket.send(sentence)

modified_message =client_socket.recv(2048).decode()
print(f'From server[{server_name}:{server_port}]: {modified_message}')

client_socket.close()