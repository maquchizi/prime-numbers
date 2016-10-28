from math import sqrt


def generate_prime_numbers(finish):
    for number in range(0, finish):
        if isPrime(number):
            print number


def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    else:
        for count in range(2, int(sqrt(number))):
            if number % count == 0:
                return False
            return True
