import socket
import pickle

def GET():
    return 'Oi'
def POST():
    return 'Oi'
def PUT():
    return 'Oi'
def DELETE():
    return 'Oi'

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
          
        mensagem = pickle.loads(mensagem)
        print("[{},{}]: {}".format(cliente[0],cliente[1], mensagem))

        if mensagem == 'GET':
            mensagem = GET()
        elif mensagem == 'POST':
            mensagem = POST()
        elif mensagem == 'PUT':
            mensagem = PUT()
        elif mensagem == 'DELETE':
            mensagem = DELETE()
        elif mensagem == 'CLOSE':
            mensagem = 'Conexão encerrada'
        elif mensagem == 'HELP':
            mensagem = 'Os comandos que você pode utilizar são: GET, POST, PUT, DELETE, CLOSE.'
        else:
            mensagem = 'O comando escolhido não é suportado'

        resposta = pickle.dumps(mensagem)
        conexao.send(resposta) # Envio da resposta à solicitação feita

        if mensagem == 'Conexão encerrada':
            conexao.close()
            break
        
    print("[{},{}]: FOI DESCONECTADO".format(cliente[0],cliente[1]))
    conexao.close()
