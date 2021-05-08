from socket import *

#porta do servidor
serverPort = 12110

# cria socket TCP
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(1)

# 
print ("Server ON ... ")
print ("Aguardando mensagens ... ")


while 1:
    # servidor aguarda por requisições
    connectionSocket, addr = serverSocket.accept()
     
    # leitura da mensagem enviada pelo cliente na porta 1024
    sentence = connectionSocket.recv(1024)

    # mostra a mensagem recebida do cliente
    print ("Mensagem Recebida: ", sentence.decode() , " de ", addr)
	 
    # realiza a modificação da mensagem para UpperCase
    capitalizedSentence = sentence.upper()
	 
    # envia essa mensagem modificada para o cliente
    connectionSocket.send(capitalizedSentence)

    # mostra a mensagem enviada para cliente
   # print ("Mensagem Enviada: ", capitalizedSentence)
	 
    # fecha a conexão
connectionSocket.close()
