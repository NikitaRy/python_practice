"""
Как мы видим MyPy ругается: https://drive.google.com/file/d/1u9UzqSJM2N6qD6fjeL8iCOFYZiMHylNZ/view?usp=sharing (там .png-шник с его руганью)
"""

from math import ceil, floor, pow

first_primes: list[int]
first_primes = [2, 3, 5, 7, 11, 13, 17, 19.0]  # 19.0 != int


def is_prime(n: int) -> bool:

    d: int
    p: int
    q: int
    k: int
    a: int
    b: int  # должен быть float

    if n in first_primes:
        return True
    if n % 2 == 0:
        return False
    d = ceil(pow(n, (1/3)))
    for p in range(2, d+1):
        if n % p == 0:
            return False
    for k in range(1, d+1):
        p = ceil(pow(4*k*n, 0.5))
        q = floor(pow(4*k*n, 0.5) + pow(n, 1/6)/pow(16*k, 0.5))
        for a in range(p, q+1):
            b = pow((a**2-4*k*n), 0.5)
            if int(b) == b:
                return False
    return True


"""
Проверяем, есть ли опечатки в книге О. Германа (знаю его лично, а следовательно, доверяю)
Но: доверяй,но проверяй => реализуем проверку на простоту классическим способом
"""


def is_prime_naive(n: int) -> bool:

    i: int

    if n <= 2:
        return True
    for i in range(2, ceil(pow(n, 0.5))+1):
        if n % i == 0:
            return False
    return 1  # 1 = int != bool

# Сравниваем результат работы двух алгоритмов


j: int

for j in range(2, 100000):
    if is_prime(j) != is_prime_naive(j):
        print("Паника!!! ", j)
# Я проверил на небольших числах -- пока что только треск сверчков
