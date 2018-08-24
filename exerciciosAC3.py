dicionario_teste = {111: 'Nome1' , 222: 'Nome2', 333: 'Nome3'}

class Contato:
    
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def imprime(self):
        return "Nome: {} , Telefone: {} , E-mail: {}".format(self.nome, self.telefone, self.email)

    def reset(self):
        self.nome = None
        self.telefone = None
        self.email = None


def conta_elementos(dicionario):
    return len(dicionario)


def verifica_presenca(dicionario, chave):
    if chave in dicionario.keys():
        return True
    else:
        return False


def insere(dicionario, chave, objeto):
    if chave not in dicionario.keys():
        dicionario[chave] = objeto
        return True
    else:
        return False


def remove(dicionario, chave):
    if chave in dicionario:
        del dicionario[chave]
        print(dicionario)
        return True
    else:
        return False



def imprime(dicionario):
    print("+ Iniciando - Imprimindo informacoes do dicionario:")

    for chave, valor in dicionario.items():
        print ("Chave [{}] : valor [{}]".format(chave, valor))

    print("+ Finalizando - Imprimindo informacoes do dicionario:")

#TESTES DAS FUNÇÕES ABAIXO

#print ( remove(dicionario_teste, 222) )
#print(imprime(dicionario_teste))
#obj = Contato('Rodrigo', 3781, 'rodrigo@uol')
#obj.imprime()
#print( insere(dicionario_teste, 666, 'Nome3') )
#print(verifica_presenca(dicionario_teste, 242))
#print(conta_elementos(dicionario_teste))