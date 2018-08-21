telefones = ['3781-5431', '96670-8268', '3782-9862', '3781-5431', '5621-9874', '96652-3654', '3234-5678', '96541-2589', '3782-9862', '3781-5431']

def conta_elementos(lista):

    return print(len(lista))

def verifica_presenca(lista, telefone):

    if telefone in lista:
        return True
    else:
        return False

def insere(lista, telefone):

    if telefone not in lista:
        lista.append(telefone)
        return True
    else:
        return False

def remove(lista, telefone):

    if telefone in lista:
        for tel in lista:
            if tel == telefone:
                lista.remove(telefone)
        return True
    else:
        return False

def imprime(lista):

    indice = 0
    print('+ Iniciando - Imprimindo informacoes da lista:')

    for tel in lista:
        print("índice[{}] : valor[{}]".format(indice, tel))
        indice += 1

    print('+ Finalizando - Imprimindo informacoes da lista:')





print(imprime(telefones))