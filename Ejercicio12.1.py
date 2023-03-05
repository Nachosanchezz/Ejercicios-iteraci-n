def cuadrados_perfectos(limite):
    lista = []
    i = 0
    while i**2 < limite:
        lista.append(i**2)
        i += 1  
    return lista

