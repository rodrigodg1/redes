import socket
from datetime import datetime
#lado cliente para enviar a leitura do sensor de temperatura para um servidor 
# o cliente pode ser replicado
while True:

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('192.168.1.11', 11123))

        print("Msg do Servidor: ", client.recv(1024).decode())

        
        #para esse exemplo é enviado ao servidor o horario da leitura
        data_e_hora_atuais = datetime.now()
        sensor = "Temperatura"
        hora_leitura = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        leitura = input('Temperatura Atual: ')

        #constrói a msg a ser enviada
        msg = f"{sensor}: {leitura} em [{hora_leitura}]"

        msg = str(msg)
        print(msg)
        #envia ao servidor
        client.send(bytes(msg, "utf-8"))

        

        client.close()

    except:
        print("Erro de comunicação com o servidor !")
        break



    
    



