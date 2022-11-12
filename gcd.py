def gcd(first_number, second_number):
    if second_number == 0:
        return first_number
    return gcd(second_number, first_number % second_number)


a = int(input('Enter a: '))
b = int(input('Enter b: '))

print('gcd(a,b) = ', gcd(a, b))
