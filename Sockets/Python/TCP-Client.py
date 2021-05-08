
from socket import *

#ip do servidor TCP
serverName = "192.168.1.11"

#porta do servidor TCP
serverPort = 12110


while True:
    #socket
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # abre a conexão TCP
    clientSocket.connect((serverName,serverPort))

    # mensagem do usuario
    sentence = input("Digite uma mensagem: ")

    #envia a msg para o socket
    clientSocket.send(bytes(sentence, "utf-8"))

    #mostra a mensagem enviada ao servidor
    print ("Mensagem enviada ao servidor:  ", sentence)

    #recebe a mensagem modificada pelo servidor
    #na porta 1024
    modifiedSentence = clientSocket.recv(1024)

    # mostra a mensagem recebida do servidor
    print ("Mensagem recebida do servidor: ", modifiedSentence)

    # fecha a conexão TCP
    clientSocket.close()
