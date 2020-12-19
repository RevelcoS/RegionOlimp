import unittest
from union import union

class UnionTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(list(union([], [])), [])
    
    def test_1_elemental(self):
        self.assertEqual(list(union([1], [2])), [])
        self.assertEqual(list(union([1], [1])), [1])

    def test_main(self):
        self.assertEqual(list(union([4, 4, 1, 2, 7, 6], [10, 10, 6, 8, 8, 9, 9, 9, 3])), [6])
        self.assertEqual(list(union([8, 7, 6, 6, 4, 5, 1, 2, 3], [1, 2, 3, 5, 6, 6, 6])), [1, 2, 3, 5, 6])
    
    def test_all_equal(self):
        self.assertEqual(list(union([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])), [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == "__main__":
    unittest.main()