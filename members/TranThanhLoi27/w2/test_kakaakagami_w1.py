import sys
from pathlib import Path

# Automatically add REPO_ROOT to sys.path to resolve internal member imports
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from members.KaKaAkagami.w1.translate import primes_up_to

# --- W1-4: translate.primes_up_to -----------------------------------------


def test_primes_up_to_small_bounds():
    """Verify correct prime generation for small typical upper bounds."""
    # When n = 2, the only prime is [2]
    assert primes_up_to(2) == [2]
    # When n = 3, the primes are [2, 3]
    assert primes_up_to(3) == [2, 3]
    # When n = 10, the primes are [2, 3, 5, 7]
    assert primes_up_to(10) == [2, 3, 5, 7]


def test_primes_up_to_invalid_and_edge_bounds():
    """EDGE CASE: Verify that inputs less than 2 safely return an empty list."""
    assert primes_up_to(1) == []
    assert primes_up_to(0) == []
    assert primes_up_to(-5) == []


def test_primes_up_to_when_n_is_a_prime():
    """Verify the inclusive upper bound condition when n itself is a prime number."""
    # 13 is prime, so 13 must be included as the last element of the output list
    result = primes_up_to(13)
    assert result[-1] == 13
    assert result == [2, 3, 5, 7, 11, 13]


def test_primes_up_to_when_n_is_a_composite_square():
    """Verify behavior when n is a composite perfect square (e.g., 25 = 5*5)."""
    # Ensures the isqrt(n) + 1 loop correctly reaches 5 and marks its multiples
    result = primes_up_to(25)
    assert 25 not in result
    assert result[-1] == 23  # The largest prime <= 25 is 23


def test_primes_up_to_large_bound():
    """Verify sieve accuracy on a larger scale up to 100."""
    result = primes_up_to(100)
    # Mathematically, there are exactly 25 prime numbers between 2 and 100
    assert len(result) == 25
    # Spot-check specific boundaries and composite values
    assert result[0] == 2
    assert result[-1] == 97
    assert 91 not in result  # 91 is a composite number (13 * 7)
