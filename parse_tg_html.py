###################################################                                                                                                        #
# Simple Telegram's HTML exported messages parser #
###################################################
from bs4 import BeautifulSoup #type: ignore
import argparse
import typing
import pathlib
import time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple util to extract msgs from TG chat history")
    parser.add_argument("path", type=pathlib.Path, help="Provide input path")
    parser.add_argument("result", type=pathlib.Path, help="Provide output path")
    args = parser.parse_args()
    return args


def read_contents(dir: pathlib.Path) -> typing.List[str]:
    files: typing.List[pathlib.Path]
    things: typing.List[str]
    files = sorted(pathlib.Path(dir).rglob("*.html"))
    things = []
    for elem in files:
        with open(elem, "r") as f:
            page = f.read()
        soup = BeautifulSoup(page, "lxml")
        for tag in soup.find_all("div", "text"):
            element = tag.get_text()
            if (
                len(element) >= 35
                and len(element) <= 100
                and not "@" in element
                and not "//" in element
                and element[1 : element.index("\n", 3) + 1] not in things
            ):
                things.append(element[1 : element.index("\n", 3) + 1])
    return sorted(things)


def write_contents(
    contents: typing.List[str], path: pathlib.Path = pathlib.Path("test.txt")
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
    print("--- Чтение выполнено за %.2f сек ---" % (time.time() - start_time))
    write_contents(contents, args.result)
    print("--- Общее время выполнения %.2f сек ---" % (time.time() - start_time))
