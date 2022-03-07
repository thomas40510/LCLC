% LCLC séance 1
% guilers

# Opérateurs
Entrer chaque ligne dans la console Python. Regarder le résultat.
```python
print(2 + 3)
print(6 - 2)
print(2 * 6)

n = 3
m = 42
print(n, m)
print(n * m)

print(m / n)
print(m // n)
print(m % n)

print(n == m)
print(n != m)
print(n == 42)
print(n == '42')

print(n > 20)
print(n <= 40)

y = n + n
print(y)
```

# If then else
## 1. Nombres pairs
Écrire un script Python qui, pour un nombre ```n``` choisi, dit s'il est pair ou impair.

[//]: # (```python)

[//]: # (n = 3  # nombre choisi)

[//]: # ()
[//]: # (if n % 2 == 0:)

[//]: # (    print&#40;"Le nombre est pair !"&#41;)

[//]: # (else:)

[//]: # (    print&#40;"Le nombre est impair..."&#41;)

[//]: # (```)


## 2.
[//]: # (TODO)

# Boucles for
## 1. somme des entiers
Écrire un script Python qui donne la somme des nombres entiers de 1 à 20.

Existe-t-il un moyen plus simple de programmer cette somme ?

[//]: # (### 1&#41; "En dur" :)

[//]: # (```python)

[//]: # (x = 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20)

[//]: # ()
[//]: # (print&#40;x&#41;)

[//]: # (```)

[//]: # ()
[//]: # (### 2&#41; avec une boucle :)

[//]: # (```python)

[//]: # (y = 0)

[//]: # (for i in range&#40;21&#41;:)

[//]: # (    y += i)

[//]: # ()
[//]: # (print&#40;y&#41;)

[//]: # (```)


## 2. Tables de multiplication

Écrire un script Python qui détaille la table de 3.

Comment le programmer plus simplement ?

[//]: # (### 1&#41; "en dur":)

[//]: # (```python)

[//]: # (print&#40;'3 * 0 =', 3&#41;)

[//]: # (print&#40;'3 * 1 =', 6&#41;)

[//]: # (print&#40;'3 * 2 =', 9&#41;)

[//]: # (...)

[//]: # (print&#40;'3 * 10 =', 30&#41;)

[//]: # (```)

[//]: # (### 2&#41; avec boucle ```for``` :)

[//]: # (```python)

[//]: # (for i in range&#40;11&#41;:)

[//]: # (    print&#40;f'3 * {i} =', 3 * i&#41;)

[//]: # (```)

# Boucles while

## 1. Quotient d'une division
Écrire un script Python qui, à l'aide d'une boucle ```while```, calcule pour deux nombres ```a``` et ```b``` le quotient de la division de ```a``` par ```b```.

[//]: # (```python)

[//]: # (a = 42  # nbre de départ &#40;dividende&#41;)

[//]: # (b = 3  # nbre par lequel on divise &#40;diviseur&#41;)

[//]: # ()
[//]: # (q = 0)

[//]: # ()
[//]: # (while a >= b:)

[//]: # (    a = a - b)

[//]: # (    q = q + 1)

[//]: # ()
[//]: # (print&#40;q&#41;)

[//]: # (print&#40;a // b == q&#41;)

[//]: # (```)


## 2. Avion
Un avion, initialement à 11 000 mètres d'altitude, descend de 300 mètres chaque minute. Au bout de combien de temps passera-t-il sous les 2000 m d'altitude ?

Écrire un script permettant d'avoir la réponse.

[//]: # (```python)

[//]: # (h = 11000)

[//]: # (t = 0)

[//]: # (while h >= 2000:)

[//]: # (    h = h - 300)

[//]: # (    t = t + 1)

[//]: # (print&#40;t&#41;)

[//]: # (```)


# BOSS FINAL : conjecture de Syracuse
Les règles :
- on choisit un nombre entier supérieur à 0 ;
- s'il est pair : on le divise par 2 ; 
- s'il est impair : on le multiplie par 3 et on ajoute 1 ;
- on recommence jusqu'à obtenir 1.

=> Programmer cet algorithme sur Python.

[//]: # (```python)

[//]: # (n = 42  # nombre de départ)

[//]: # (while n != 1:)

[//]: # (    if n % 2 == 0 :)

[//]: # (        n = n // 2)

[//]: # (    else:)

[//]: # (        n = n * 3 + 1)

[//]: # (    print&#40;n&#41;)

[//]: # (print&#40;n&#41;)

[//]: # (```)

# LE BOSS FINAL MAIS LE VRAI CETTE FOIS QU'ON AVAIT PAS VU VENIR DERRIÈRE LE PREMIER BOSS FINAL : ??