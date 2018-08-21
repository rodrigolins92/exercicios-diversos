def SaoVogais(letra):
    vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vogal in vogais:
        if letra == vogal:
            return print("1")
    return print("0")

SaoVogais("d")