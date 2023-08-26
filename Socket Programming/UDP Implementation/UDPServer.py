from socket import *

server_port = int(input('Enter server port number: '))
server_socket = socket(AF_INET, SOCK_DGRAM) # IPv4 + UDP
server_socket.bind(('', server_port))

print('[+] The server is ready to receive.')

while True:
    message, client_address = server_socket.recvfrom(2048)
    modified_message = message.decode().upper()
    server_socket.sendto(modified_message.encode(), client_address)
