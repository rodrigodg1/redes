from socket import *

# Define a porta do servidor
serverPort = 12000

# Cria um novo socket do tipo TCP (SOCK_STREAM) e endereçamento IPv4 (AF_INET)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Associa o socket ao endereço IP e porta especificados
serverSocket.bind(("10.62.9.237", serverPort))

# Define o socket para ouvir conexões, com uma fila de no máximo 1 conexão pendente
serverSocket.listen(1)

print("O servidor está pronto para receber conexões")

# Loop infinito para lidar com conexões de clientes
while True:
    # Aceita uma nova conexão de cliente e retorna um novo socket e o endereço do cliente
    connectionSocket, addr = serverSocket.accept()
    print("Conectado com: [", addr[0], "Porta:", addr[1], "]")

    # Recebe até 1024 bytes de dados do cliente e decodifica a mensagem como string
    sentence = connectionSocket.recv(1024).decode()

    # Converte a mensagem recebida para letras maiúsculas
    capitalizedSentence = sentence.upper()

    # Envia a mensagem em maiúsculas de volta ao cliente, codificando-a como bytes
    connectionSocket.send(capitalizedSentence.encode())

    # Fecha a conexão com o cliente
    connectionSocket.close()
    print("Conexão com: [", addr[0], "Porta:", addr[1], "] foi fechada")
