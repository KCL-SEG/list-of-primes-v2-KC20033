"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    start = 2
    if number_of_primes > 0:

        while len(list) != number_of_primes:
        
            if checkPrime(start):
                list.append(start)
            start += 1
        
    else:
        raise ValueError        
        
    return list


def checkPrime(x):
    if x <= 1 :
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True
