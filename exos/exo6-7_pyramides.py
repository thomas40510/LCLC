def pyramide(n):
    """
    Affiche une pyramide de n lignes
    :param n: nombre de lignes
    """
    for etage in range(1, n+1):  # chaque étage de la pyramide
        for nb in range(1, etage+1):  # chaque nombre jusqu'au numéro de l'étage
            print(nb, end=" ")  # on affiche les nombres séparés par une espace
        print()  # on revient à la ligne entre chaque étage


def pyramide_retour(n):
    pyramide(n)  # début de la pyramide : c'est une pyramide simple
    for etage in range(n-1, 0, -1):  # étages de la pyramide retour
        for nb in range(1, etage+1):
            print(nb, end=" ")
        print()
