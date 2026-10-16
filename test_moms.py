import unittest

from moms import moms


class TestMoms(unittest.TestCase):

    def test_positive_price(self):
        self.assertEqual(
            moms(100, 25),
            125
        )
    def test_negative_price(self):
        self.assertEqual(
            moms(-100, 25),
            125
        )
    def test_absurdly_high_price(self):
        with self.assertRaisesRegex(
            ValueError,
            "Absurdly high price"
        ):
            moms(1_000_001, 25)

    def test_illegal_tax_zero(self):
        with self.assertRaisesRegex(
            ValueError,
            "Illegal tax"
        ):
            moms(100, 0)
	
    def test_illegal_tax_over_100(self):
        with self.assertRaisesRegex(
            ValueError,
            "Illegal tax"
        ):
            moms(100, 101)

if __name__ == "__main__":
    unittest.main()
