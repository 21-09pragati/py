def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes(n):
    """Print all prime numbers up to n."""
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)

# Example usage
n = 50  # Change this value to print prime numbers up to a different number
print_primes(n)
