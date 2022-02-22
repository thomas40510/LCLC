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

