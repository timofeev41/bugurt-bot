import argparse
import pathlib
import typing
import random


def parse_args() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description="Simple Bugurt Generator v0.0.1")
        parser.add_argument("path", type=pathlib.Path, help="Provide input path")
        args = parser.parse_args()
        return args


def get_words(target: pathlib.Path) -> typing.Tuple[str]:
        with open(target, "r") as f:
                contents = f.read().split("\n")
        return contents


def bugurt(words: typing.List[str], x: int = 10) -> None:
        for iter in range(x + 1):
                if random.randrange(1, 100) < 10:
                        print(" ' "  + random.choice(words) + " ' ")
                else:
                        print(random.choice(words))
                if iter < x:
                        print("@@@")


if __name__ == "__main__":
        args = parse_args()
        data = get_words(args.path)
        bugurt(data)