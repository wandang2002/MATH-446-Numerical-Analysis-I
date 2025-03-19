import unittest
import numpy as np
import numpy.testing as npt
from AdditionInBase2 import add_integral, add_fractional, add_binary, main_func
class TestBinaryMethods(unittest.TestCase):
    
    def test_add_integral(self):
        x = np.array([1, 0, 0, 1, 1, 1])
        y = np.array([1, 1, 1, 1])
        z = add_integral(x, y)
        npt.assert_array_equal(z, np.array([1, 1, 0, 1, 1, 0]))

    def test_add_fractional(self):
        x = np.array([1, 1, 1, 1])
        y = np.array([1, 1, 1])
        I, F = add_fractional(x, y)
        self.assertEqual(I, 1)
        npt.assert_array_equal(F, np.array([1, 1, 0, 1]))

    def test_add_binary(self):
        Ix = np.array([1, 0, 0, 1, 1, 1])
        Iy = np.array([1, 1, 1, 1])
        Fx = np.array([1, 1, 1, 1])
        Fy = np.array([1, 1, 1])
        I, F = add_binary(Ix, Fx, Iy, Fy)
        npt.assert_array_equal(I, np.array([1, 1, 0, 1, 1, 1]))
        npt.assert_array_equal(F, np.array([1, 1, 0, 1]))
    
    def test_main(self):
        Fy = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        Fx = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        I, F, E = main_func(Fx, Fy)
        self.assertEqual(I, 1)
        npt.assert_array_equal(F, np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual(E, 1)
        
if __name__ == '__main__':
    unittest.main()
