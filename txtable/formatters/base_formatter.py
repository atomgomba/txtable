import os
from abc import abstractmethod
from collections.abc import Sequence

from ..options_merger import OptionsMerger


class BaseFormatter(metaclass=OptionsMerger):
    options = {
        "header_separator": True
    }
    width = -1
    height = -1
    raw_column_widths = []

    def __init__(self, **kwargs):
        self.options.update(kwargs)

    def format(self, rows: Sequence) -> str:
        table = []
        last_row = len(rows) - 1
        for row_index, columns in enumerate(rows):
            formatted_columns = []
            for column_index, value in enumerate(columns):
                column_width = self.raw_column_widths[column_index]
                formatted_columns.append(self.format_cell(value, column_width, column_index, row_index))
            if 0 == row_index and self.header_separator:
                table.append(self.format_header(formatted_columns))
            elif last_row == row_index:
                table.append(self.format_footer(formatted_columns))
            else:
                table.append(self.format_row(formatted_columns, row_index))
        return os.linesep.join(table)

    @abstractmethod
    def format_header(self, columns: list) -> str:
        pass

    @abstractmethod
    def format_row(self, columns: list, row_index: int) -> str:
        pass

    # noinspection PyUnusedLocal
    @staticmethod
    def format_cell(value, column_width: int, column_index: int, row_index: int) -> str:
        if row_index == 0:
            return "{:<{w}s}".format(str(value), w=column_width)
        else:
            return "{:>{w}s}".format(str(value), w=column_width)

    # noinspection PyUnusedLocal
    @staticmethod
    def format_footer(columns: list) -> str:
        return ""

    def __getattr__(self, name: str):
        return self.options.get(name)
