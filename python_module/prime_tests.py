from math import ceil, floor, pow


def is_prime_naive(n):
    if n <= 2:
        return True
    for i in range(2, ceil(pow(n, 0.5))+1):
        if n % i == 0:
            return False
    return True


def leman_method(n):
    first_primes = [2, 3, 5, 7, 11, 13, 17, 19]  # Алгоритм работает на нечетных, больше 21;
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
