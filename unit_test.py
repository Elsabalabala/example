#!usr/bin/env python
#coding=utf-8

import nwmath
import unittest

class multiplyTest(unittest.TestCase):
    '''
    Test the multiplyTest from the nwmath library
    '''
    def test_multiply_integer(self):
        """
        Test that subtracting integers returns the correct result
        """
        result=nwmath.multiply(3, 4)
        self.assertEqual(result, 12)

if __name__ =='__main__':
    unittest.main()
