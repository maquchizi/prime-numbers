from math import sqrt


def generate_prime_numbers(finish):
    '''
        Loop through all number from 0 to finish
        Check if number is prime
        Print it if it is otherwise, ignore
    '''
    for number in range(0, finish):
        if is_prime(number):
            print number


def is_prime(number):
    '''
        Check if a number is a prime
        Return True if it is otherwise, False
    '''
    if number < 2:
        return False
    if number == 2:
        return True
    else:
        '''
            For speed, only test till sqrt of number
            If no match found in this first partion, there will be none in the next partition till number
        '''
        for count in range(2, int(sqrt(number))):
            if number % count == 0:
                return False
            return True
