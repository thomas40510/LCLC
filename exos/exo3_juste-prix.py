def situe_nombre(n, p):
    """
    Situe p par rapport à n
    :param n: nombre cherché
    :param p: prix proposé
    """
    if n < p:
        return "plus petit"
    elif n > p:
        return "plus grand"
    else:
        return "juste"


def juste_prix(n):
    """
    Permet de jouer au juste prix
    :param n: nombre à chercher
    """
    nb_essais = 10  # nombre d'essais accordés
    for essai in range(nb_essais):  # on recommence tant qu'il reste des essais
        prix = int(input("Entrez un prix : "))
        situe = situe_nombre(n, prix)
        if situe == 'juste':
            print("Bravo !")
            return True  # on arrête si le juste prix est trouvé
        else:
            print("Le prix cherché est " + situe)
