import itertools

first_factorials = [1, 1]


class Factorialinf:
    class _Factorialinf_iter:
        def __init__(self):
            self.i = 0
            self.factorials = first_factorials

        def Factorials_generate(self):
            # нам достаточно первые два значения факториала, чтобы далее генирировать
            self.factorials.append(self.factorials[-1] * self.i)

        def __next__(self):
            j = self.i
            self.i += 1
            if self.i >= 2:
                self.Factorials_generate()  # собственно: зачем нам лишние числа в начале массива с факториалами?
            return self.factorials[j]

    def __iter__(self):
        return Factorialinf._Factorialinf_iter()


number_of_iters = int(input())
Factorials = Factorialinf()
print(*itertools.islice(Factorials, number_of_iters))
