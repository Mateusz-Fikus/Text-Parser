import argparse
from functions.objects import Parse



def main():

    parser = argparse.ArgumentParser(description="Case converter - tab/space or space/tab")

    parser.add_argument("-f", "--from", required=False, choices=['tabs', 'spaces'], type=str, help="From which case")
    parser.add_argument("-r", "--replace", action="store_true", required=False, help="Overwrite the file")
    parser.add_argument("-t", "--tab-chars",  required=False, type=int, help="How many spaces for tab", default=4)
    parser.add_argument("file", metavar="file", help="File name")

    args = parser.parse_args()
    Parse(case=args.__dict__["from"], rep=args.__dict__["replace"], tabc=args.__dict__["tab_chars"], file=args.__dict__["file"]).parsing()


if __name__=="__main__":
    main()
