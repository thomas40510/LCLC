def trouveur_code(n):
    for mil in range(10):
        for cent in range(10):
            for diz in range(10):
                for unit in range(10):
                    code = mil * 1000 + cent * 100 + diz * 10 + unit
                    if code == n:
                        return code


# autre solution :
def trouveur_code_2(n):
    for code in range(10000):
        if code == n:
            return code


# un peu de maths : pour un code à 4 chiffres, 10 * 10 * 10 * 10 = 10000 solutions
# pour un code à 5 chiffres, 10 * 10 * 10 * 10 * 10 = 100000 solutions
# pour un code à 6 chiffres, 10 * 10 * 10 * 10 * 10 * 10 = 1000000 solutions !
