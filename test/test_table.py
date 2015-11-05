from unittest import TestCase

from txtable import TextTable


class TestTable(TestCase):

    def test_normalize(self):
        # single column 1
        t = TextTable([1, 2, 3, 4, 5, 6])
        result = t.rows
        self.assertEqual(result, [[1], [2], [3], [4], [5], [6]])

        # single column 2
        t = TextTable([1, [2], 3, 4, 5, 6])
        result = t.rows
        self.assertEqual(result, [[1], [2], [3], [4], [5], [6]])

        # rows of unequal column number 1
        t = TextTable([[1, 2], [3], [4, 5, 6]])
        result = t.rows
        self.assertEqual(result, [[1, 2, None], [3, None, None], [4, 5, 6]])

        # rows of unequal column number 2
        t = TextTable([[1, 2], 3, [4, 5, 6]])
        result = t.rows
        self.assertEqual(result, [[1, 2, None], [3, None, None], [4, 5, 6]])

        # correct table
        t = TextTable([[1, 2], [3, 4], [5, 6]])
        result = t.rows
        self.assertEqual(result, [[1, 2], [3, 4], [5, 6]])
