import argparse
import pathlib
import typing
import random


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple Bugurt Generator v0.0.1")
    parser.add_argument("path", type=pathlib.Path, help="Provide input path")
    parser.add_argument("--size", type=int, default=10, help="Enter output lenght")
    parser.add_argument("--option", type=str, default=None, help="Enter options for output")
    args = parser.parse_args()
    return args


def get_words(target: pathlib.Path, options: typing.Optional[str]) -> typing.List[str]:
    with open(target, "r") as f:
        contents = f.read().split("\n")
    if options is not None:
        filtered: typing.List[str]
        filtered = []
        for line in contents:
            if options.upper() in line:
                filtered.append(line)
        if not len(filtered):
            raise Exception(f"There is no {options} in {args.path}")
        return filtered
    else:
        return contents


def bugurt(words: typing.List[str], output_size: int = 10) -> None:
    for iter in range(output_size):
        choice = random.choice(words).upper()
        if random.randrange(1, 100) < 10:
            print(f"'{choice}'")
        else:
            print(choice)
        if iter < output_size - 1:
            print("@@@")


if __name__ == "__main__":
    args = parse_args()
    data = get_words(args.path, args.option)
    bugurt(data, args.size)
