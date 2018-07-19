from .default_formatter import DefaultFormatter


class MdFormatter(DefaultFormatter):
    options = {
        "header_separator": "-",
        "column_spacing": " | ",
    }
