class Lista2a:
    def __init__(self, lista):
        self.lista_interna = lista
    
    def adicionar(self, elemento):
        self.lista_interna.append(elemento)

    def remover(self, indice):
        del self.lista_interna[indice]

    def imprime(self):
        print(self.lista_interna)

listas_2a = [
    Lista2a([1,2,3]),
    Lista2a([4,5,6]),
    Lista2a([7,8,9])
]

for lista in listas_2a:
    lista.remover(0)
    lista.lista_interna

#print(listas_2a[1].lista_interna)

