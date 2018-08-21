"""
Abrir, procurar, escrever em arquivos txt...
w --> write, escrever
r --> read, ler
a --> append, expandir
"""



nomeArquivo = input("Qual o nome do arquivo?")


arquivoUsuario = open(nomeArquivo, 'w') #Aqui ele criou o arquivo "nomeArquivo" porque não existia

arquivoUsuario.write('Rodrigo\nRoberto\nFernanda\nMarcia')

#LENDO INFORMAÇÕES DO ARQUIVO


arquivoUsuario = open(nomeArquivo, 'r')

print(arquivoUsuario.readlines())

arquivoUsuario.close()

arquivoUsuario = open(nomeArquivo, 'a')

arquivoUsuario.write('\nNovo Nome')

print(arquivoUsuario.readlines())


arquivoUsuario.close()
