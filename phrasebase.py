import os
import json
import re
from tqdm import tqdm
from colorama import Fore, init
import argparse


# set path to the directory where the paper jsons are located.
path ="./Papers"


def main():
    parser = argparse.ArgumentParser(
        description="Searches through thousands of papers and tries to match a certain input string")

    parser.add_argument('--IGNORECASE', dest='IGNORECASE', action='store_true',
                        help="By default search is case sensetive. If you dont want this, set this flag.")

    parser.add_argument("--exact", dest='exact', action='store_true',
                        help="By default it also matches substrings. If you only want exct matches, set this flag")

    args = parser.parse_args()

    # important for colorama on windows
    init()

    pattern = input("What string are you searching for? (Regex are allowed): ")

    if args.IGNORECASE and args.exact:
        pattern = pattern.strip()
        pattern = re.compile(f" {pattern} ", flags=re.IGNORECASE)

    elif args.IGNORECASE:
        pattern = re.compile(pattern, flags=re.IGNORECASE)

    elif args.exact:
        pattern = pattern.strip()
        pattern = re.compile(f" {pattern} ")

    for file in tqdm(os.listdir(path)):
        j = json.load(open(os.path.join(path, file)))

        paper_id = j["paper_id"]

        for text in j["body_text"]:
            if re.search(pattern, text["text"]):
                paragraph = text["text"]
                print(f"\n\nPaper ID: {paper_id}")
                match = re.search(pattern, paragraph).group()
                print(re.sub(match, Fore.RED + match + Fore.RESET, paragraph), end="\n\n")

    # TODO: paralize


if __name__ == '__main__':
    try:
        main()
    # prevents error when pressing ctrl+c
    except KeyboardInterrupt:
        pass
