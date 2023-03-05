class Palabra:
    def __init__(self, palabra, anterior, siguiente):
        self.palabra = palabra
        self.anterior = anterior
        self.siguiente = siguiente

def palabras_con_letra(letra, diccionario, anterior, siguiente):
    lista = []
    i = 0
    while i < len(diccionario) and diccionario[i].palabra[0] < letra:
        i += 1
    while i < len(diccionario) and diccionario[i].palabra[0] == letra:
        lista.append(diccionario[i])
        i += 1
   
    return lista
        