"""
Sorteio - Crie uma lista com o nome de 10 pessoas, 
embaralhe esta lista e sorteie uma pessoa, 
depois embaralhe novamente e sorteie outra pessoa, 
lembrando que não poderá ser a mesma pessoa a ser sorteada.
"""

import random

pessoas = ['Rodrigo', 'Roberto', 'Fernanda', 'Marcia', 'Carlos', 
            'Maria', 'Fred', 'Ronaldo', 'Marcos', 'Joana']


random.shuffle(pessoas)

print(pessoas)

pessoa1 = random.choice(pessoas)
pessoa2 = random.choice(pessoas)

while pessoa1 == pessoa2:
    pessoa2 = random.choice(pessoas)

print('%s / %s' %(pessoa1, pessoa2))

x = 0
while x < len(pessoas):
    if pessoas[x] == pessoa1:
        print("%s no ítem %i da lista" %(pessoa1,x))
    if pessoas[x] == pessoa2:
        print("%s no ítem %i da lista" %(pessoa2,x))
    x += 1

