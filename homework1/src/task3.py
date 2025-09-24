#Checks if number is positive, negative, or zero
def check_number(n):
    #if greater than zero
    if n > 0:
        return "positive"
    #if less than zero
    elif n < 0:
        return "negative"
    #otherwise
    return "zero"

#Returns the first 10 prime numbers
def first_primes(count=10):
    primes, num = [], 2
    while len(primes) < count:
        if all(num % p != 0 for p in range(2, int(num**0.5)+1)):
            primes.append(num)
        num += 1
    return primes

#Gives a summation from 1 to 100
def sum_1_to_100():
    total, i = 0, 1
    while i <= 100:
        total += i
        i += 1
    return total