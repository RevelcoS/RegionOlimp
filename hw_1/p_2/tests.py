import unittest
from parentheses import parantheses

class ParanthesesTest(unittest.TestCase):

    def test0(self):
        self.assertTrue(parantheses(0) == [""])

    def test1(self):
        self.assertEqual(parantheses(1), ["()"])

    def test2(self):
        self.assertEqual(parantheses(2), ["(())", "()()"])

    def test3(self):
        self.assertEqual(parantheses(3), ["((()))","(()())","(())()","()(())","()()()"])

if __name__ == "__main__":
    unittest.main()