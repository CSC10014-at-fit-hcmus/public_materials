from math import isqrt


def primes_up_to(n: int) -> list[int]:
    """Return all primes up to n using the Sieve of Eratosthenes.

    Unlike C++ vector<bool>, Python uses a list of booleans.
    """
    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    return [i for i in range(2, n + 1) if is_prime[i]]
