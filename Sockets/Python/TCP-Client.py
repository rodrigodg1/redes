#Socket TCP

from socket import *

# Define o endereço IP e a porta do servidor
serverName = "10.62.9.237"
serverPort = 12000

# Cria um novo socket do tipo TCP (SOCK_STREAM) e endereçamento IPv4 (AF_INET)
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Tenta conectar ao servidor usando o endereço IP e a porta especificados
    clientSocket.connect((serverName, serverPort))
    print("Conectado com o Servidor:", serverName, "Porta:", serverPort)

    # Solicita ao usuário que insira uma frase em letras minúsculas
    sentence = input("Digite uma frase em letras minúsculas: ")

    # Envia a frase codificada como bytes para o servidor
    clientSocket.send(sentence.encode())

    # Recebe até 1024 bytes de dados do servidor e decodifica a mensagem como string
    modifiedSentence = clientSocket.recv(1024)
    print("Do Servidor:", modifiedSentence.decode())

    # Fecha a conexão com o servidor
    clientSocket.close()

except:
    print("Falha ao conectar")
