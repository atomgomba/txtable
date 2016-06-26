from unittest import TestCase

from txtable import TextTable


class TestDefaultFormatter(TestCase):

    def test_format(self):
        data = [['Value A', 'Value B', 'Value C'], [1, 2, 10], [30, 4, 5], [5, 60, 1]]
        t = TextTable(data)
        expected = """Value A  Value B  Value C
=======  =======  =======
      1        2       10
     30        4        5
"""
        self.assertEqual(str(t), expected)
