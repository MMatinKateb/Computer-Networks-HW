from socket import *

server_name = input('Enter hostname: ')
server_port = int(input('Enter port number: '))

# Client socket with IPv4 addressing & UDP protocol
client_socket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')

client_socket.sendto(message.encode(), (server_name, server_port))

modified_message, server_address = client_socket.recvfrom(2048)

print(f'From server [{server_name}:{server_port}]: {modified_message.decode()}')

client_socket.close()