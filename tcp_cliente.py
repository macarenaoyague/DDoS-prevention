from socket import *

serverName = '40.124.98.131'
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = 'paquete tcp'

clientSocket.send(bytes(sentence, 'UTF-8'))
modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence)
clientSocket.close()
