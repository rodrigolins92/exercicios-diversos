seu_nome = str(input("Digite o seu nome completo: ")).strip()

print("Seu nome em maiúsculas é: {}"
      .format(seu_nome.upper())
      )

print("Seu nome em minúsculas é: {}"
      .format((seu_nome.lower()))
      )

print("Seu nome ao todo tem {} letras"
      .format(len(seu_nome) - seu_nome.count(' '))
      )

print('Seu primeiro nome tem {} letras'
      .format(seu_nome.find(' '))
      )

separa = seu_nome.split()

print(separa)