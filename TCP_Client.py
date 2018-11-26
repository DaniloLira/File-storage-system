# coding=UTF-8

import socket
import pickle

def entrar_cadastrar():

    escolha = ''
    while escolha != '1' and escolha != '2':
        escolha = input('Você deseja entrar ou criar uma nova conta ? (1 - entrar, 2- criar conta): ')

    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    resposta = conexao_inicial(escolha,login,senha)

    while resposta == '1' or resposta == '2':
        
        if resposta == '1':
            print('Login já cadastrado, tente novamente com outro login')
            login = input('Digite seu login: ')

            resposta = conexao_inicial(escolha,login,senha)

        elif resposta == '2':
            print('Usuário ou senha incorretos, tente novamente')
            login = input('Digite seu login: ')
            senha = input('Digite sua senha: ')

            resposta = conexao_inicial(escolha,login,senha)

    IP = resposta[0]
    PORTA = resposta[1]

    credenciais = (login,senha)
    conexao_real(IP, PORTA, credenciais)

    
        
def conexao_inicial(escolha,login,senha):
    '''
        Essa função serve para estabelecer conexão com o servidor
        de autenticação. Para não estabelecer logo a comunicação
        com o servidor de arquivos, a gente criou um servidor pra
        receber o login e verificar no banco de dados, caso as cre-
        denciais estejam armazenadas, o servidor envia uma mensagem
        contendo a porta do servidor de sistemas de arquivos e ai
        a outra funçãoo é chamada
    '''
    
    IP = '192.168.0.6'
    PORTA = 32421

    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect((IP, PORTA))
    
    credenciais = (escolha,login,senha)
    credenciais = pickle.dumps(credenciais)
    cliente.send(credenciais)
    resposta = cliente.recv(1024)
    cliente.close()
    resposta = pickle.loads(resposta)

    return resposta


def conexao_real(IP, PORTA, credenciais):
    '''
        Essa função serve para estabelecer conexão com o servidor
        dos arquivos, recebendo a porta vinda do servidor de autenticação
    '''
    
    cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect((IP, PORTA))

    while True: 
        mensagem = input("Digite sua mensagem: ")
               
        cliente.send(pickle.dumps(mensagem))

            
        #Recebimento da resposta do servidor ÃƒÂ  solicitaÃƒÂ§ÃƒÂ£o
            
        resposta = cliente.recv(1024) # DefiniÃƒÂ§ÃƒÂ£o da quantidade de Bytes recebida.
        resposta = pickle.loads(resposta) # DecodificaÃƒÂ§ÃƒÂ£o da resposta.
        print("[{},{}]: {}".format(IP, PORTA, resposta))

        if resposta == 'Conexão encerrada': break

    cliente.close()


if __name__ == '__main__': 
    entrar_cadastrar()


