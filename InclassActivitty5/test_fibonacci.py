import unittest
import fibonacci
number=0
result=fibonacci.average()
factorial=fibonacci.factorial


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(result,233)
    def test3(self):
        self.assertTrue(result,1)

class TestCase(unittest.TestCase):
    def test1(self):
        number=5
        self.assertEqual(factorial(5),120)
    def test3(self):
        self.assertTrue(factorial(3),6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
