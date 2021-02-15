import pathlib
import typing
import random


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
            raise Exception(f"There is no {options}")
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

