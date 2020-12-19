
#UDP CLIENT

#ESSE CÓDIGO PODERÁ SER EXECUTADO EM DIFERENTES COMPUTADORES PARA TER MAIS CLIENTES COMUNICANDO COM O SERVIDOR

from socket import *

# alterar para o endereço ip do servidor UDP
serverName = "192.168.1.11"

# alterar para a porta do servidor UDP
# deve ser a mesma
serverPort = 12000

while True:
    #cria um socket UDP
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    #texto de entrada do usuário
    message = input("Digite uma mensagem:")

    #envia a msg do usuario para o servidor
    clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))

    print ("Mensagem enviada para o servidor: ", message)

    # recebe a msg modificada pelo servidor (UPPER CASE)
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    # mostra no terminal a mensagem modificada pelo Servidor
    print ("Recebido do Servidor: ", modifiedMessage)

    # Finaliza a conexão com o socket
    clientSocket.close()
