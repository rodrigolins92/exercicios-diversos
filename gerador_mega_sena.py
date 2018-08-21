from random import randint

def gera_jogos(qtd_jogos):

    contador_jogos = 0

    while contador_jogos < qtd_jogos:

        lista = []
        contador_numeros = 0

        while contador_numeros < 6:
            numero_sorteado = randint(1,60)
            if numero_sorteado not in lista:
                lista.append(numero_sorteado)
                contador_numeros += 1

        lista.sort()
        lista_string = '-'.join(map(str,lista))
        print(lista_string)

        contador_jogos += 1

#Programa principal abaixo =D

print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("---- GERADOR DE JOGOS DA MEGA SENA ----")
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("")
print("")

qtde_jogos = int(input("Quantidade de jogos que deseja criar --> "))

print("")
print("")

gera_jogos(qtde_jogos)
print("")