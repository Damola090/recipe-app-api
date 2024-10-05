"""
sample tests

"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """
    Test the Calc Module
    """

    def test_add_numbers(self):
        """Test Adding Numbers Together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test Subracting Numbers From Eachother"""
        res = calc.subtract(10, 8)

        self.assertEqual(res, 2)
        