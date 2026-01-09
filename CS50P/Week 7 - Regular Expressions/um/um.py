import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    pattern = r'\bum\b'
    count = re.findall(pattern, s)
    return len(count)


if __name__ == "__main__":
    main()
