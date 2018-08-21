lista_fibo = []
auxiliar1 = 1
auxiliar2 = 1


lista_fibo.append(auxiliar1)
for i in range(10):
    auxiliar1 = auxiliar2 - auxiliar1
    auxiliar2 += auxiliar1
    lista_fibo.append(auxiliar2)

print(lista_fibo)

