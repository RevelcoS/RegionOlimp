import unittest
from min_diff import min_diff

class TestMinDiff(unittest.TestCase):

    def test_simple(self):
        # test lst: [1, 3, 1]
        # all difs: [0, 2, 2]
        test_lst = [1, 3, 1]
        self.assertEqual(min_diff(test_lst, 1), 0)
        self.assertEqual(min_diff(test_lst, 2), 2)
        self.assertEqual(min_diff(test_lst, 3), 2)

    def test_main(self):
        # test lst: [1, 3, 1, 10, 15, 7, 20]
        # all diffs: [0, 2, 2, 4, 3, 5, 5, 6, 6, 7, 8, 9, 9, 10, 12, 13, 14, 14, 17, 19, 19]
        test_lst = [1, 3, 1, 10, 15, 7, 20]
        self.assertEqual(min_diff(test_lst, 1), 0)
        self.assertEqual(min_diff(test_lst, 2), 2)
        self.assertEqual(min_diff(test_lst, 4), 4)
        self.assertEqual(min_diff(test_lst, 8), 6)
        self.assertEqual(min_diff(test_lst, 10), 7)
        self.assertEqual(min_diff(test_lst, 14), 10)
        self.assertEqual(min_diff(test_lst, 20), 19)
        self.assertEqual(min_diff(test_lst, 21), 19)
        

if __name__ == "__main__":
    unittest.main()