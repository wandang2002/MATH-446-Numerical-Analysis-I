import unittest
import numpy as np
import numpy.testing as npt
from LUFactorization import generate_random_vectors, gauss_for_special_matrices_less_memory, generate_matrix

class TestLUMethods(unittest.TestCase):

    def test_gauss_for_special_matrices(self):
        numtest = 10
        for i in range(numtest):
            a, b, c = generate_random_vectors(n = 3, rand = numtest)
            orginal_matrix = generate_matrix(a, b, c)
            L, a, b, c = gauss_for_special_matrices_less_memory(a, b, c)
            U = generate_matrix(a, b, c)
            npt.assert_array_almost_equal(np.dot(L,U), orginal_matrix)


if __name__ == '__main__':
    unittest.main()
