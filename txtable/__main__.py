from sys import exit, stdin
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import json
import csv

from . import TextTable
from .formatters import BaseFormatter, DefaultFormatter, HeadlessFormatter, MdFormatter, RstFormatter


def get_formatter(name: str) -> BaseFormatter or None:
    name = str(name).lower()
    if name == "default":
        return DefaultFormatter()
    if name == "headless":
        return HeadlessFormatter()
    if name == "md":
        return MdFormatter()
    if name == "rst":
        return RstFormatter()
    return None


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
    table = list(csv.reader(f))
    f.close()
    return table


def main(args):
    formatter = get_formatter(args.formatter)
    if not formatter:
        print("ERROR: Invalid formatter: " + args.formatter)
        return 1
    if not args.files:
        if args.type == "json":
            data = stdin.read()
            table = create_json_table(data)
        elif args.type == "csv":
            table = create_csv_table(stdin)
        else:
            print("ERROR: Unknown data format")
            return 1
        print(TextTable(table, formatter=formatter))
        return 0
    for path in args.files:
        with open(path) as f:
            if path.endswith(".json"):
                table = create_json_table(f.read())
            elif path.endswith(".csv"):
                table = create_csv_table(f)
            else:
                print("ERROR: Unknown data format")
                return 1
        print(path + ": ")
        print(TextTable(table, formatter=formatter))
        print("\n")
    return 0


if __name__ == "__main__":
    parser = ArgumentParser(prog="txtable", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("files", default=[], nargs="*", help="Path to input files (json/csv) or read from stdin when empty")
    parser.add_argument("-f", "--formatter", default="default", help="Table format: default, headless, md (Markdown) or rst (ReStructuredText)")
    parser.add_argument("-t", "--type", default="json", help="Input data type to read from stdin: json/csv")

    exit(main(parser.parse_args()))
