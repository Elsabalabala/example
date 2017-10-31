#!usr/bin/env python
#coding=utf-8

import nwmath
import unittest

class addTest(unittest.TestCase):
    '''
    Test the multiplyTest from the nwmath library
    '''
    def test_add_integer(self):
        """
        Test that subtracting integers returns the correct result
        """
        result=nwmath.add(3, 4)
        self.assertEqual(result, 7)


class divideTest(unittest.TestCase):
    '''
    Test the multiplyTest from the nwmath library
    '''
    def test_divide_integer(self):
        """
        Test that subtracting integers returns the correct result
        """
        result=nwmath.divide(64, 4)
        self.assertEqual(result, 16)

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
