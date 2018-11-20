import socket
import pickle

def cadastrar(credenciais, lista_credenciais, arquivo):
    ''' A função apenas adiciona na lista 'credenciais' as
        credenciais cadastradas do novo usuário '''
    print(lista_credenciais)
    print(credenciais)
    for dados in lista_credenciais: 
        if credenciais[0] == dados[0]: return False
    
    lista_credenciais.append(credenciais)
    atualizar(arquivo,credenciais)
    return True 

def logar(credenciais, lista_credenciais):
    print(credenciais)
    if credenciais in lista_credenciais: return True
    
    return False

def atualizar(arquivo, credenciais):
    arq = open(arquivo,'a')

    arq.write(credenciais[0]+'\n')
    arq.write(credenciais[1]+'\n')
    arq.close()
    
    

def ler_arquivo(arquivo):
    ''' FunÃ§Ã£o pra ler o arquivos da base de dados e adicionar numa lista '''
    
    arq = open(arquivo,'r')
    login = 'X'
    lista = []
    
    while login != '':
        login = arq.readline()
        senha = arq.readline()
        
        login = login[:len(login)-1]
        senha = senha[:len(senha)-1]
        
        lista.append((login,senha))

    return lista

def armazenar(lista_credenciais, nome_arq):
    arq = open(nome_arq,'w')

    for tupla in lista_credenciais:
        for credencial in tupla: arq.write(credencial+'\n')

    arq.close()
            

lista_credenciais = ler_arquivo('banco_de_dados.txt') 

IP = '192.168.0.6'
PORTA = 32421

endereco = (IP, PORTA) # DefiniÃƒÂ§ÃƒÂ£o da dupla identificadora do socket
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # CriaÃƒÂ§ÃƒÂ£o do socket
servidor.bind(endereco) # Amarrando a tupla ao socket
print("Servidor Ligado\n")
servidor.listen(5) # DeterminaÃƒÂ§ÃƒÂ£o de quantas conexÃƒÂµes serÃƒÂ£o escutadas


while True: # LaÃƒÂ§o da conexÃƒÂ£o
    conexao, cliente = servidor.accept()
    print("Conectado por Ip: {} Porta: {}".format(cliente[0],cliente[1]))

    while True:
        mensagem = conexao.recv(1024) #quantos bits o servidor recebe de uma sÃƒÂ³ vez
        if not mensagem: break
          
        mensagem = pickle.loads(mensagem)
        print("[{},{}]: {}".format(cliente[0],cliente[1], mensagem))
        
        if mensagem[0] == '1':
            resposta = logar(mensagem[1:], lista_credenciais)

            if resposta == True:
                autenticacao = (IP,32420)
            elif resposta == False:
                autenticacao = '2'
                
        elif mensagem[0] == '2':
            resposta = cadastrar(mensagem[1:], lista_credenciais, 'banco_de_dados.txt')
                    
            if resposta == True:
                autenticacao = (IP,32420)
            elif resposta == False:
                autenticacao = '1'

        conexao.send(pickle.dumps(autenticacao)) # Envio da resposta ÃƒÂ  solicitaÃƒÂ§ÃƒÂ£o feita

    print("[{},{}]: FOI DESCONECTADO".format(cliente[0],cliente[1]))
    conexao.close()
    
