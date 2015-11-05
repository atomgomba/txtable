from collections.abc import Sequence

from .formatters import BaseFormatter, DefaultFormatter


class TextTable:

    __rows = []

    def __init__(self, rows: Sequence=None, formatter: BaseFormatter=None):
        """
        :param rows: Table data
        :param formatter: A formatter instance
        """
        if isinstance(rows, Sequence):
            self.rows = rows
        self.formatter = formatter or DefaultFormatter()

    def get_max_column_number(self) -> int:
        """
        :return: the number of columns in the longest row
        """
        width = 0
        for row in self.rows:
            try:
                n = len(row)
            except TypeError:
                n = 1
            if width < n:
                width = n
        return width

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

    def __normalize(self) -> list:
        if not self.rows:
            self.__rows = []
            return
        max_width = self.get_max_column_number()
        normal = []
        for row in self.rows:
            if not row:
                normal.append([None] * max_width)
                continue
            if not isinstance(row, Sequence):
                v = [row]
            else:
                v = row
            w = len(v)
            if w < max_width:
                v = v + [None] * (max_width - w)
            normal.append(v)
        self.__rows = normal

    def __str__(self):
        if not self.rows:
            return ""
        if not isinstance(self.rows[0], Sequence):
            raise ValueError("Input data doesn't seem to be tabular")
        self.formatter.width = len(self.rows[0])
        self.formatter.height = len(self.rows)
        self.formatter.raw_column_widths = self.get_column_widths()
        return self.formatter.format(self.rows)
