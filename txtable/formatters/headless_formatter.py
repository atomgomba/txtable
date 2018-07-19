from .default_formatter import DefaultFormatter


class HeadlessFormatter(DefaultFormatter):
    options = {
        "header_separator": False,
    }
