def SaoIguais(a, b, c):
    if (a == b) and (b == c):
        return print("São Iguais")
    else:
        return print("São diferentes")

x1 = input("Primeira letra: ")
x2 = input("Segunda letra: ")
x3 = input("Terceira letra: ")

resposta = SaoIguais(x1, x2, x3)

