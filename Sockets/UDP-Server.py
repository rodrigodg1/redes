from socket import *

#porta do servidor UDP
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("O servidor está pronto para receber")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()

    #mostra a mensagem recebida
    print("> ", message.decode() ,"      de ", clientAddress)

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
