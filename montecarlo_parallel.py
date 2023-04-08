from multiprocessing.pool import Pool
from math import sin, pi
import random

""" Считаем интеграл $\int_{0}^{\pi} \frac{sin(x)}{x} \dot dx$"""


def montecarlo(n):
    a = 0
    b = pi
    points_number = 0
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, 1)
        if y <= sin(x) / x:
            points_number += 1
    return pi * points_number / n


def montecarlo_parallel(n):
    integral = 0
    pool = Pool()
    for result in pool.map(montecarlo, [n for _ in range(4)]):
        integral += result
    return integral


if __name__ == "__main__":
    n = 10000
    print(montecarlo_parallel(n) / 4)
