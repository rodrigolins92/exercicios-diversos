palavra = 'hello world'
dicionario = {}
for letra in palavra:
    if letra not in dicionario:
        dicionario[letra] = 1
    else:
        dicionario[letra] += 1

print(dicionario)