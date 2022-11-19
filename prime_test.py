import math

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Is not prime"
    return "Is prime"

def generator(n):
    k = n/math.log(n)
    arr = []
    primes = 0
    while len(arr) < k+1:
        primes += 1
        if is_prime(primes) == "Is prime":
            arr.append(primes)
    if arr.count(n):
        return "Is prime"
    return "Is not prime"
