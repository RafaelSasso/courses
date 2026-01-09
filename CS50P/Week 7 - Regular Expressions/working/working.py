import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    pattern = r'([0-9]{2}|[1-9])(:[0-9]{2})? (AM|PM) to ([0-9]{2}|[1-9])(:[0-9]{2})? (AM|PM)'
    if matches := re.search(pattern, s):
        groups = matches.groups()

        def newTime(h,m,p):
            if m == ":60":
                raise ValueError
            if m == None:
                m = ":00"
            h = int(h)
            if p == "PM":
                if h != 12:
                    h += 12
            else:
                if h == 12:
                    h=0

            return f'{h:02}{m}'
        h1=newTime(groups[0],groups[1],groups[2])
        h2=newTime(groups[3],groups[4],groups[5])

        return f'{h1} to {h2}'
    else:
        raise ValueError


if __name__ == "__main__":
    main()
