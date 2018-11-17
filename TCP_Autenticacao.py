import socket


def ler_arquivo(arquivo):
    ''' Função pra ler o arquivos da base de dados e adicionar numa lista '''
    
    arq = open(arquivo,'r')
    login = 'X'
    lista = []
    
    while login != '':
        login = arq.readline()
        senha = arq.readline()
        
        login = login[:len(login)-1]
        senha = senha[:len(senha)-1]
        
        lista.append(('{} {}').format(login,senha))

    return lista

credenciais = ler_arquivo('banco_de_dados.txt')
print(credenciais)  

IP = '192.168.0.6'
PORTA = 32421

endereco = (IP, PORTA) # DefiniÃ§Ã£o da dupla identificadora do socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # CriaÃ§Ã£o do socket

servidor.bind(endereco) # Amarrando a tupla ao socket
print("Servidor Ligado\n")

servidor.listen(5) # DeterminaÃ§Ã£o de quantas conexÃµes serÃ£o escutadas


while True: # LaÃ§o da conexÃ£o
    conexao, cliente = servidor.accept()
    print("Conectado por Ip: {} Porta: {}".format(cliente[0],cliente[1]))

    while True:
        mensagem = conexao.recv(1024) #quantos bits o servidor recebe de uma sÃ³ vez
        if not mensagem: break
          
        mensagem = mensagem.decode()
        print("[{},{}]: {}".format(cliente[0],cliente[1], mensagem))
        
        if mensagem in credenciais:
            resposta = ('32420')
        else:
            resposta = ('00000')
            
        conexao.send(resposta.encode()) # Envio da resposta Ã  solicitaÃ§Ã£o feita

    print("[{},{}]: FOI DESCONECTADO".format(cliente[0],cliente[1]))
    conexao.close()
