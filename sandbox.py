print("hello world!")


def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


# 1 to 100
L = [x for x in range(1, 100) if is_prime(x)]
print(len(L))
