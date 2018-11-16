import socket

IP = '192.168.0.6'
PORTA = 32420

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cliente.connect((IP, PORTA))


while True: # Laço da conexão
    mensagem = input("Digite sua mensagem: ")

    if not mensagem: print("CONEXÃO ENCERRADA\n"); break
    
    else:          
        cliente.send(mensagem.encode())

        
        #Recebimento da resposta do servidor à solicitação
        
        resposta = cliente.recv(1024) # Definição da quantidade de Bytes recebida.
        resposta = resposta.decode() # Decodificação da resposta.
        print("[{},{}]: {}".format(IP, PORTA, resposta))

cliente.close()
    
        
