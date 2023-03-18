def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise 
    """
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True 

def find_primes(numbers):
    """
    Retruns a new list containing only the prime numbers from the input list
    """
    primes = [] 
    for n in numbers:
        if is_prime(n):
            primes.append(n)
    return primes

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = find_primes(numbers)
print(primes)  # Output: [2, 3, 5, 7]
