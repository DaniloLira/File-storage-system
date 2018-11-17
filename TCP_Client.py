import socket

def conexao_inicial():
    '''
        Essa função serve para estabelecer conexão com o servidor
        de autenticação. Para não estabelecer logo a comunicação
        com o servidor de arquivos, a gente criou um servidor pra
        receber o login e verificar no banco de dados, caso as cre-
        denciais estejam armazenadas, o servidor envia uma mensagem
        contendo a porta do servidor de sistemas de arquivos e ai
        a outra função é chamada
    '''
    
    IP = '192.168.0.6'
    PORTA = 32421

    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect((IP, PORTA))

    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    credenciais = ('{} {}').format(login,senha)

    cliente.send(credenciais.encode())
    resposta = cliente.recv(1024)
    cliente.close()
    resposta = resposta.decode()

    return resposta


def conexao_real(PORTA):
    '''
        Essa função serve para estabelecer conexão com o servidor
        dos arquivos, recebendo a porta vinda do servidor de autenticação
    '''
    
    IP = '192.168.0.6'

    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect((IP, PORTA))

    while True: # LaÃ§o da conexÃ£o
        mensagem = input("Digite sua mensagem: ")

        if not mensagem: print("CONEXÃƒO ENCERRADA\n"); break
        
        else:          
            cliente.send(mensagem.encode())

            
            #Recebimento da resposta do servidor Ã  solicitaÃ§Ã£o
            
            resposta = cliente.recv(1024) # DefiniÃ§Ã£o da quantidade de Bytes recebida.
            resposta = resposta.decode() # DecodificaÃ§Ã£o da resposta.
            print("[{},{}]: {}".format(IP, PORTA, resposta))

    cliente.close()


resposta = conexao_inicial()

if resposta == '00000': 
    print('CRIAR FUNÇÃO DE CADASTRO')
else:
    print('Conexão Estabelecida Com Sucesso !!')
    conexao_real(int(resposta))


