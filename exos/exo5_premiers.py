def est_premier(n):
    """
    Teste si un nombre est premier
    :param n: nombre à tester
    :return: True si n est premier, False sinon
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def premiers(n):
    """
    Donne les n premiers nombres premiers
    :param n: nombre de premiers à afficher
    """
    liste = []
    for nombre in range(1, n + 1):
        if est_premier(nombre):
            liste.append(nombre)
