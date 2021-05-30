import socket

#lista para armazenar os dados
dados_lista = []



portaServidor = 11123
ip_servidor = "192.168.1.11"


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ip_servidor,portaServidor))

serverSocket.listen()

print("Server ON")

while True:

    client, address = serverSocket.accept()
    print("Conectado com {}".format(str(address)))

    client.send("Informe a leitura do sensor".encode('ascii'))

    dados = client.recv(1024).decode()
    
    #adiciona na lista
    dados_lista.append(dados)


    #mas tbm pode adicionar diretamentee no arquivo
    f = open("dados.txt", "a")
    f.write("\n")
    f.write(dados)
    f.close()

    client.close()









