import argparse
from gendiff.diff_builder import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff")

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", default="stylish")

    args = parser.parse_args()

    print(
        generate_diff(
            args.first_file,
            args.second_file,
            args.format,
        )
    )