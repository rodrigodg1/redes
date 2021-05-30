from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)

print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connected with: [", addr[0] , "Port:", addr[1], "]")
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
    print("Connection with: [", addr[0] , "Port:", addr[1], "] was closed")

