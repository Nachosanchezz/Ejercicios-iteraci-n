def palabras_con_letra(letra, diccionario, siguiente, anterior):
    lista = []
    i = 0
    while i < len(diccionario) and diccionario[i][0] < letra:
        i += 1
    while i < len(diccionario) and diccionario[i][0] == letra:
        lista.append(diccionario[i])
        i += 1
    if siguiente:
        while i < len(diccionario) and diccionario[i][0] == siguiente:
            lista.append(diccionario[i])
            i += 1
    if anterior:
        i = i - 2
        while i >= 0 and diccionario[i][0] == anterior:
            lista.append(diccionario[i])
            i -= 1
    return lista

