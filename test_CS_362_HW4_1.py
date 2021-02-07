import unittest
import CS_362_HW4_1
result=CS_362_HW4_1.cubevolume(6)
array=CS_362_HW4_1.average()
name=CS_362_HW4_1.name()

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(result,216)
    def test2(self):
        self.assertGreater(result,0)
    def test3(self):
        self.assertTrue(result,216)

class TestCasetwo(unittest.TestCase):
    def test4(self):
        self.assertEqual(array,10)
    def test5(self):
        self.assertGreater(array,0)
    def test6(self):
        self.assertTrue(array,10)

class TestCasethree(unittest.TestCase):
    def test7(self):
        self.assertEqual(name,"NateHill")
    def test8(self):
        self.assertFalse(result,"NateHill")
    def test9(self):
        self.assertTrue(result,"NateHill")

if __name__ == '__main__':
    unittest.main(verbosity=2)
