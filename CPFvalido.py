

cpf = input("Digite o cpf -> ")

cpf_lista = []
cpf_lista_original = []

for i in range(len(cpf)):
    cpf_lista.append(int(cpf[i]))

cpf_lista = cpf_lista_original

if len(cpf_lista) != 11 or cpf == 11111111111 or cpf == 22222222222 or cpf == 33333333333 or cpf == 44444444444 or cpf == 55555555555 or cpf == 66666666666 or cpf == 77777777777 or cpf == 88888888888 or cpf == 99999999999 or cpf == 00000000000:
    print("CPF inválido...")
else:
    cpf_lista.pop(10)
    print(cpf_lista)
    del(cpf_lista[9,10])
    print(len(cpf_lista))
    primeiro_digito = 10
    soma_primeiro_digito = 0
    for i in range(9):
        soma_primeiro_digito += (primeiro_digito * cpf_lista[i])
        primeiro_digito = primeiro_digito - 1

"""
auxiliar = (( soma_primeiro_digito * 10 ) % 11)
if auxiliar == 10:
    cpf_lista.append(0)
else:
    cpf_lista.append(auxiliar)

primeiro_digito = 11
soma_primeiro_digito = 0
for i in range(10):
    soma_primeiro_digito += (primeiro_digito * cpf_lista[i])
    primeiro_digito = primeiro_digito - 1

auxiliar = (( soma_primeiro_digito * 10 ) % 11)
if auxiliar == 10:
    cpf_lista.append(0)
else:
    cpf_lista.append(auxiliar)

if cpf_lista == cpf_lista_original:
    print("CPF válido!!!")
else:
    print("CPF inválido!!!")
print(cpf_lista)

"""