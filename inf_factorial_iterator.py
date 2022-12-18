import itertools

first_factorial = 1
second_factorial = 1


class Factorialinf:
    class _Factorialinf_iter:
        def __init__(self):
            self.i = 0
            self.factorial1 = first_factorial
            self.factorial2 = second_factorial

        def Factorials_generate(self):
            # нам достаточно первые два значения факториала, чтобы далее генирировать
            self.factorial2 = self.factorial2 * self.i

        def __next__(self):
            j = self.i
            self.i += 1
            if self.i >= 2:
                self.Factorials_generate()  # собственно: зачем нам лишние числа в начале массива с факториалами?
            return self.factorial2

    def __iter__(self):
        return Factorialinf._Factorialinf_iter()


number_of_iters = int(input())
Factorials = Factorialinf()
print(*itertools.islice(Factorials, number_of_iters))
