import os

from . import BaseFormatter


class DefaultFormatter(BaseFormatter):
    options = {
        "header_separator": "=",
        "column_spacing": "  ",
    }

    def format_header(self, columns: list) -> str:
        header = self.column_spacing.join(columns) + os.linesep
        header += self.column_spacing.join([self.header_separator * len(col) for col in columns])
        return header

    def format_row(self, columns: list, row_index: int) -> str:
        return self.column_spacing.join(columns)
