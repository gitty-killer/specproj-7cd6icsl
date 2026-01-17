"""CLI entry point."""

import sys
from etl.pipeline import run


def main():
    out = run(sys.stdin.readlines())
    for line in out:
        print(line)


if __name__ == '__main__':
    main()
