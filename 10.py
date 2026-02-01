def splaszcz_liste(elementy):
    splaszczona = []
    for x in elementy:
        if isinstance(x, list):
            splaszczona.extend(splaszcz_liste(x))
        else:
            splaszczona.append(x)
    return splaszczona

lista = [1, [2, 3], 4, [5, [6, 7]]]

print(splaszcz_liste(lista))