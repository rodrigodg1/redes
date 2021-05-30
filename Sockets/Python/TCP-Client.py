#Socket TCP

from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 

try:
    clientSocket.connect((serverName,serverPort)) 
    print("Connected with Server:", serverName , "Port:", serverPort)
    sentence = input("Input lowercase sentence: ")
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print("From Server: ", modifiedSentence.decode())
    clientSocket.close()

except:
    print("Fail to connect")