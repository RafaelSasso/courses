import sys


def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        print(f'{read_lines(sys.argv[1])}')

def read_lines(f):
    split = f.split(".")
    if (split == f) or (split[1] != "py"):
        sys.exit("Not a Python file")
    else:
        count=0
        try:
            with open(f) as file:
                for line in file:
                    line = line.strip()
                    if (line != "") and (not line.startswith("#")):
                        count+=1
        except FileNotFoundError:
            sys.exit("File does not exist")
    return count

if __name__ == "__main__":
    main()
