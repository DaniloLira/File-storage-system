import socket


IP = '192.168.0.6'
PORTA = 32420

endereco = (IP, PORTA) # Definição da dupla identificadora do socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Criação do socket

servidor.bind(endereco) # Amarrando a tupla ao socket
print("Servidor Ligado\n")

servidor.listen(5) # Determinação de quantas conexões serão escutadas


while True: # Laço da conexão
    conexao, cliente = servidor.accept()
    print("Conectado por Ip: {} Porta: {}".format(cliente[0],cliente[1]))

    while True:
        mensagem = conexao.recv(1024) #quantos bits o servidor recebe de uma só vez
        if not mensagem: break
          
        mensagem = mensagem.decode()
        print("[{},{}]: {}".format(cliente[0],cliente[1], mensagem))

        if mensagem == 'GET':
            pass
        elif mensagem == 'POST':
            pass
        elif mensagem == 'PUT':
            pass
        elif mensagem == 'DELETE':
            pass

        resposta = mensagem.encode()
        conexao.send(resposta) # Envio da resposta à solicitação feita

    print("[{},{}]: FOI DESCONECTADO".format(cliente[0],cliente[1]))
    conexao.close()
