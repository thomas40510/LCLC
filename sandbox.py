print("hello world!")


def nombres_pairs(liste):
    liste_pairs = []
    for nombre in liste:
        if nombre % 2 == 0:
            liste_pairs.append(nombre)
    return liste_pairs
