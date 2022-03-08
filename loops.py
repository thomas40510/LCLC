""" exo 1 : somme des entiers de 0 à 20
1) "en dur"
2) avec boucle
"""
x = 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20

print(x)

y = 0
for i in range(21):
    y += i

print(y)

print('3*1 =', 3)

for i in range(11):
    print(f"print('3 * {i} =', 3*i)")

n = 42  # nombre de départ
while n != 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
print(n)

code = 2242
N = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for c1 in N:
    for c2 in N:
        for c3 in N:
            for c4 in N:
                tentative = c1 * 1000 + c2 * 100 + c3 * 10 + c4
                if tentative == code:
                    print("Trouvé !", tentative)
                    quit()
                else:
                    print('Dommage...', tentative)
