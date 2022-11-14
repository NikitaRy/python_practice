def egcd(first_number, second_number):
    if first_number == 0:
        return second_number, 0, 1
    gcd, x, y = egcd(second_number % first_number, first_number)
    return gcd, y - (second_number // first_number) * x, x


a = int(input('Enter a: '))
b = int(input('Enter b: '))

print(egcd(a, b))
