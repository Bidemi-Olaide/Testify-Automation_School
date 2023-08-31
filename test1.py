
import main
import unittest

class TestMain(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(main.addition(1, 2), 3, "Should be 3")
        self.assertEqual(main.addition(10, 7), 17, "Should be 17")
        self.assertEqual(main.addition(8, 22), 30, "Should be 30")
        self.assertEqual(main.addition(-5, 9), 4, "Should be 4")
    def test_subtraction(self):
        self.assertEqual(main.subtraction(8, 2), 6, "Should be 6")
if __name__ == '__main__':
    unittest.main()