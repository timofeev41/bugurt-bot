import argparse
import pathlib
import typing
import random


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple Bugurt Generator v0.0.1")
    parser.add_argument("path", type=pathlib.Path, help="Provide input path")
    parser.add_argument("--size", type=int, default=10, help="Enter output lenght")
    args = parser.parse_args()
    return args


def get_words(target: pathlib.Path) -> typing.List[str]:
    with open(target, "r") as f:
        contents = f.read().split("\n")
    return contents


def bugurt(words: typing.List[str], output_size: int = 10) -> None:
    for iter in range(output_size + 1):
        if random.randrange(1, 100) < 10:
            print(f"'{random.choice(words)}'")
        else:
            print(random.choice(words))
        if iter < output_size:
            print("@@@")


if __name__ == "__main__":
    args = parse_args()
    data = get_words(args.path)
    bugurt(data)
