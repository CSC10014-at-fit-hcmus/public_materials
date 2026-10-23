
"""W2-4: Cross-member tests for Dang Xuan Phat's rotate_right."""

from members.Dang_Xuan_Phat.w1.translate import rotate_right


def test_rotate_right_normal():
    """Rotate a list two positions to the right."""
    assert rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_rotate_right_empty():
    """An empty list should remain empty."""
    assert rotate_right([], 3) == []


def test_rotate_right_zero_steps():
    """Rotating by zero should preserve element order."""
    assert rotate_right([1, 2, 3], 0) == [1, 2, 3]


def test_rotate_right_full_length():
    """Rotating by the list length returns the original order."""
    assert rotate_right([1, 2, 3, 4], 4) == [1, 2, 3, 4]


def test_rotate_right_large_k():
    """Steps greater than the list length should wrap around."""
    assert rotate_right([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]


def test_rotate_right_negative_k():
    """A negative right rotation behaves as a left rotation."""
    assert rotate_right([1, 2, 3, 4], -1) == [2, 3, 4, 1]


def test_rotate_right_single_element():
    """A one-element list should remain unchanged."""
    assert rotate_right([42], 100) == [42]


def test_rotate_right_does_not_modify_input():
    """Rotating should not mutate the original list."""
    original = [1, 2, 3, 4]
    result = rotate_right(original, 2)

    assert result == [3, 4, 1, 2]
    assert original == [1, 2, 3, 4]
