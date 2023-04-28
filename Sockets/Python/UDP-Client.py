from socket import *

# Define o endereço IP e a porta do servidor
serverName = "10.62.9.237"
serverPort = 12000

# Cria um novo socket do tipo UDP (SOCK_DGRAM) e endereçamento IPv4 (AF_INET)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Solicita ao usuário que insira uma frase em letras minúsculas
message = input("Digite uma frase em letras minúsculas:")

# Envia a frase codificada como bytes para o servidor
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Recebe até 2048 bytes de dados do servidor e o endereço (IP e porta) do servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Decodifica a mensagem recebida e exibe a resposta do servidor
print("Mensagem do servidor:", modifiedMessage.decode())

# Fecha o socket do cliente
clientSocket.close()
