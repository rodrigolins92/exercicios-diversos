"""
Mega Sena - Crie duas listas com números de 0 a 9,
embaralhe as listas e sorteie um número de cada uma para formar uma dezena,
repita a operação 5 vezes para sortear 5 dezenas, assim como na mega sena.
Caso a dezena caia como 00 (zero, zero) faça o sorteio dela novamente até sair outra combinação.
Depois disso exiba as dezenas sorteadas.
"""

import random

dezena = [0, 1, 2, 3, 4, 5, 6]
unidade = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

escolhidos = []

auxiliar = 0
while auxiliar < 6:
    num1 = random.choice(dezena)
    num2 = random.choice(unidade)

    if num1 == num2 and num1 == 0:
        num1 = random.choice(dezena)
        num2 = random.choice(unidade)
    numeros = str(num1) + str(num2)

    if numeros not in escolhidos:
        if int(numeros) <= 60:
            escolhidos.append(numeros)
            auxiliar += 1
    print(escolhidos)
