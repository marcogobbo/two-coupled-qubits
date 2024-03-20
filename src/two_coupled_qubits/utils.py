"""A collection of useful functions for common evaluations."""

from numpy import array, ndarray


def find_idx(data: list[float] | list[int] | ndarray, value: float | int) -> int:
    """Return the index of the array with the corresponding value."""
    if not isinstance(data, ndarray):
        data = array(data)
    return abs(data - value).argmin()
