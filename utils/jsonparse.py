import json
import argparse
import typing
import pathlib
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple util to extract msgs from TG chat history")
    parser.add_argument("path", type=pathlib.Path, help="Provide .json file path")
    parser.add_argument("result", type=pathlib.Path, help="Provide output path")
    args = parser.parse_args()
    return args


def read_contents(json_path: pathlib.Path) -> typing.Set[str]:
    result: typing.Set[str] = set()
    with open(json_path, "r") as f:
        data = json.load(f)
    messages_count = len(data["messages"])
    for element in data["messages"]:
        if not "file" in element and type(element["text"]) is str:
            message = element["text"]
            result.add(f"{message}\n")
    return result


def write_contents(
    contents: typing.Set[str], path: pathlib.Path = pathlib.Path("test.txt")
) -> None:
    option = "w"
    if pathlib.Path(path).exists():
        print(f"Found {path} file. Re(w)rite or (a)ppend data? w/a: ", end="")
        option = str(input()).lower()
    with open(path, option) as f:
        for phrase in contents:
            f.write(phrase)


if __name__ == "__main__":
    args = parse_args()
    start_time = time.time()
    contents = read_contents(args.path)
    write_contents(contents, args.result)
    print("--- Operation took %.2fs ---" % (time.time() - start_time))
