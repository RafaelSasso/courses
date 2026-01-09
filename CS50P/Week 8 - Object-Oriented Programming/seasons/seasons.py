from datetime import date
import re
import inflect
import sys


def main():
    try:
        f = format(input("Date of Birth: "))
    except ValueError:
        sys.exit('Invalid date')

    f = f.split("and ")
    newstr = ""
    for part in f:
        part.strip()
        newstr += part
    print(newstr)

def format(d):
    p = inflect.engine()
    pattern = r'^\d{4}-\d{2}-\d{2}$'

    if matches := re.fullmatch(pattern, d):
        birth = matches.group().split('-')
        birth = date(int(birth[0]), int(birth[1]), int(birth[2]))
        today = date.today()

        delta = today-birth
        delta = delta.days

        return (p.number_to_words(int(delta)*24*60)+" minutes").capitalize()
    else:
        raise ValueError


if __name__ == "__main__":
    main()
