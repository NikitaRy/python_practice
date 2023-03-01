from numpy import array
from numpy.linalg import norm
from numpy.linalg import inv
from numpy import dot
from numpy.linalg import solve as solve_out_of_the_box


def gauss(a, b):
    a = a.copy()
    b = b.copy()
    a_inversed = inv(a)  # обратная матрица
    x = dot(a_inversed, b)  # собственно решение
    return x


a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

oob_solution = solve_out_of_the_box(a, b)
solution = gauss(a, b)

print(solution)
print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
