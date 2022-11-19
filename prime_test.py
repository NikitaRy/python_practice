""" По-сути, это должно было быть улучшенным решетом Эратосфена, при использовании тождества Чебышева о количестве простых чисел, меньших n; но почему-то он не дает точного ответа на числах вида 2^n-1 """
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
    while len(arr) < 3*k+3:
        primes += 1
        if is_prime(primes) == "Is prime":
            arr.append(primes)
    if arr.count(n):
        return "Is prime"
    return "Is not prime"
