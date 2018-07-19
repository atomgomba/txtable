from collections.abc import Sequence
from typing import Optional

from .formatters import BaseFormatter, DefaultFormatter


class TextTable:

    def __init__(self,
                 rows: Optional[Sequence] = None,
                 formatter: Optional[BaseFormatter] = None):
        """
        :param rows: Table data
        :param formatter: A formatter instance
        """
        self.__rows = rows or []
        self.formatter = formatter or DefaultFormatter()
        self.__normalize()

    def get_max_column_number(self) -> int:
        """
        :return: the number of columns in the longest row
        """
        return max((len(row) if isinstance(row, Sequence) else 1 for row in self.rows))

    def get_column_widths(self) -> list:
        """
        :return: the maximum width of each column
        """
        height = len(self.rows)
        width = len(self.rows[0])
        column_widths = [0] * width
        for i in range(width):
            for j in range(height):
                v = len(str(self.rows[j][i]))
                if column_widths[i] < v:
                    column_widths[i] = v
        return column_widths

    @property
    def rows(self) -> list:
        """
        :return: the rows of the table as a list of lists
        """
        return self.__rows

    @rows.setter
    def rows(self, value: list):
        """Set the rows of the table.
        :param value: list
        """
        self.__rows = value
        self.__normalize()

    def __normalize(self):
        if not self.rows:
            self.__rows = []
            return
        max_width = self.get_max_column_number()
        normal = []
        for row in self.rows:
            if not row:
                normal.append([None] * max_width)
                continue
            v = [row] if not isinstance(row, Sequence) else row
            w = len(v)
            if w < max_width:
                v = v + [None] * (max_width - w)
            normal.append(v)
        self.__rows = normal

    def __str__(self):
        rows = self.rows
        if not rows \
                or not isinstance(rows, Sequence) \
                or 0 == len(rows) \
                or not isinstance(rows[0], Sequence) \
                or 0 == len(rows[0]):
            # data not tabular
            return ""
        self.formatter.width = len(rows[0])
        self.formatter.height = len(rows)
        self.formatter.raw_column_widths = self.get_column_widths()
        return self.formatter.format(rows)
