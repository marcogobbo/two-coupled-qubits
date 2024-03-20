"""
Test utils functions.
"""

from numpy import array

from two_coupled_qubits import find_idx


def test_find_idx():
    """
    Test find_idx function.
    """
    elements = range(100)
    ndarray_elements = array(elements)

    assert (find_idx(elements, 40), find_idx(ndarray_elements, 20)) == (40, 20)
