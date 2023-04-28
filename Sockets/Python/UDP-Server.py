from socket import *

# Define a porta do servidor
serverPort = 12000

# Cria um novo socket do tipo UDP (SOCK_DGRAM) e endereçamento IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Associa o socket à porta especificada (o endereço IP é omitido, permitindo conexões de qualquer endereço)
serverSocket.bind(("10.62.9.237", serverPort))
print("O servidor está pronto para receber")

# Loop infinito para lidar com conexões de clientes
while True:
    # Recebe até 2048 bytes de dados do cliente e o endereço (IP e porta) do cliente
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Mensagem recebida:", message, "de:", clientAddress[0], "porta:", clientAddress[1])

    # Decodifica a mensagem recebida e a converte para letras maiúsculas
    modifiedMessage = message.decode().upper()

    # Envia a mensagem em maiúsculas de volta ao cliente, codificando-a como bytes
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
