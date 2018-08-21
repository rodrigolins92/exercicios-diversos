'''
'' Dados os conhecimentos de listas que temos até agora, vamos elaborar
'' uma lista para armazenar informações de telefones.
'' A lista deverá ser criada e armazenada fora do escopo das funções para
'' ser enviada como parametro para as funções criadas.
'' Não utilizar as funções de lista (sort, max, min)
''
'''

# crie a lista aqui !!!!!!!!

telefones = ['3781-5431', '96670-8268', '3782-9862', '3781-5431', '5621-9874', '96652-3654', '3234-5678', '96541-2589', '3782-9862', '3781-5431']

'''
'' 1. Crie uma função que recebe uma lista como parametro e retorna a
''    a quantidade de elementos presentes.
''
'''
def conta_elementos(lista):

    return print(len(lista))

'''
'' 2. Crie uma função que recebe uma lista e um suposto telefone
''    e retorna um booleano informando se aquele telefone já está presente na lista
''
'''
def verifica_presenca(lista, telefone):

    if telefone in lista:
        return True
    else:
        return False

'''
'' 3. Crie uma função que recebe uma lista e um telefone como parametros
''    e armazena esta informação na lista se ela ainda não existir.
''    Se a informação existir, deverá retornar False
''    Se a informação não existir deverá retornar True
''
'''
def insere(lista, telefone):

    if telefone not in lista:
        lista.append(telefone)
        return True
    else:
        return False

'''
'' 4. Crie uma função que recebe uma lista e um telefone como parametros
''    e remove esta informação da lista se ela já existir.
''    Se a informação existir, deverá retornar True
''    Se a informação não existir deverá retornar False
''
'''
def remove(lista, telefone):

    if telefone in lista:
        for tel in lista:
            if tel == telefone:
                lista.remove(telefone)
        return True
    else:
        return False

'''
'' 5. Crie uma função que recebe uma lista como parametro
''    e imprima todos os dados presentes no console de forma ordenada (sem usar sort).
''    A saída do console deve ser exatamente:
''    + Iniciando - Imprimindo informacoes da lista:
''    índice[valor_do_indice] : valor[valor_armazenado_no_índice]
''    ...
''    índice[valor_do_indice] : valor[valor_armazenado_no_índice]
''    + Finalizando - Imprimindo informacoes da lista:
'''
def imprime(lista):

    indice = 0
    print('+ Iniciando - Imprimindo informacoes da lista:')

    for tel in lista:
        print("índice[{}] : valor[{}]".format(indice, tel))
        indice += 1

    print('+ Finalizando - Imprimindo informacoes da lista:')