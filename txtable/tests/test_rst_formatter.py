from unittest import TestCase

from ..formatters import RstFormatter
from ..table import TextTable


class TestRstFormatter(TestCase):

    def test_format(self):
        data = [['Value A', 'Value B', 'Value C'], [1, 2, 10], [30, 4, 5], [5, 60, 1]]
        fmt = RstFormatter()
        t = TextTable(data, formatter=fmt)
        expected = """+---------+---------+---------+
| Value A | Value B | Value C |
+=========+=========+=========+
|       1 |       2 |      10 |
+---------+---------+---------+
|      30 |       4 |       5 |
+---------+---------+---------+
"""
        self.assertEqual(str(t), expected)
