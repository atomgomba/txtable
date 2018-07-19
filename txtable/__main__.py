import csv
import json
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from enum import Enum
from sys import exit, stdin

from .formatters import DefaultFormatter, HeadlessFormatter, MdFormatter, RstFormatter
from .table import TextTable


class Formatter(Enum):
    default = DefaultFormatter
    headless = HeadlessFormatter
    md = MdFormatter
    rst = RstFormatter

    @staticmethod
    def enum(value: str) -> 'Formatter':
        try:
            return Formatter[value]
        except KeyError:
            raise ValueError()

    def __str__(self):
        return self.name


class DataFormat(Enum):
    csv = "csv"
    json = "json"

    @staticmethod
    def enum(value: str) -> 'DataFormat':
        try:
            return DataFormat[value]
        except KeyError:
            raise ValueError()

    def __str__(self):
        return self.name


def create_json_table(s: str) -> list:
    data = json.loads(s)
    if type(data) is not list:
        if type(data) is dict:
            data = [data]
        else:
            print(data)
            print("ERROR: JSON must contain a collection or an object")
            raise SystemExit(1)
    if 0 == len(data):
        return []
    header = list(data[0].keys())
    table = [header]
    for obj in data:
        row = []
        for column in header:
            row.append(obj.get(column))
        table.append(row)
    return table


def create_csv_table(f) -> list:
    return list(csv.reader(f))


def format_stdin(args) -> int:
    if args.type == "json":
        data = stdin.read()
        table = create_json_table(data)
    elif args.type == "csv":
        table = create_csv_table(stdin)
    else:
        print("ERROR: Unknown data format")
        return 1
    print(TextTable(table, formatter=args.formatter.value()))
    return 0


def format_files(args) -> int:
    for path in args.input:
        with open(path) as f:
            if path.endswith(".json"):
                table = create_json_table(f.read())
            elif path.endswith(".csv"):
                table = create_csv_table(f)
            else:
                print("ERROR: Unknown file format")
                return 1
        print("# %s\n" % path)
        print(TextTable(table, formatter=args.formatter.value()))
        print("\n")
    return 0


def main(args) -> int:
    return format_files(args) if args.input else format_stdin(args)


if __name__ == "__main__":
    parser = ArgumentParser(prog="txtable", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("input", default=[], nargs="*",
                        help="File paths or stdin when empty")
    parser.add_argument("-f", "--formatter", type=Formatter.enum, default=Formatter.default, choices=list(Formatter),
                        help="Select table formatter")
    parser.add_argument("-t", "--type", type=DataFormat.enum, default=DataFormat.json, choices=list(DataFormat),
                        help="Specify input data format from stdin")

    exit(main(parser.parse_args()))
