import os

from .base_formatter import BaseFormatter


class RstFormatter(BaseFormatter):

    def format_header(self, columns: list) -> str:
        header = "+-{}-+".format("-+-".join(["-" * len(col) for col in columns])) + os.linesep
        header += "| {} |".format(" | ".join(columns)) + os.linesep
        header += "+={}=+".format("=+=".join(["=" * len(col) for col in columns]))
        return header

    def format_row(self, columns: list, row_index: int) -> str:
        row = "| {} |".format(" | ".join(columns)) + os.linesep
        row += "+-{}-+".format("-+-".join(["-" * len(col) for col in columns]))
        return row
