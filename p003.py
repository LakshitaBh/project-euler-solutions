import math
N = 600851475143

def solve():
    n = N
    last_factor = None
    while n > 1:
        factor = smallest_prime_factor(n)
        last_factor = factor
        n //= factor
    return last_factor


def smallest_prime_factor(n): # smallest factor of a number is always a prime
    assert n>=2
    for factor in range(2, math.isqrt(n) + 1):
        if n % factor == 0:
            return factor
    return n  # n itself is prime


if __name__=="__main__":
    print(solve())