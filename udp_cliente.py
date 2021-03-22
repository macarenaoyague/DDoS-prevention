from socket import *

serverName = '40.124.98.131'
serverPort = 12000
message = "Paquete UDP"
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(bytes(message, 'UTF-8'), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()
