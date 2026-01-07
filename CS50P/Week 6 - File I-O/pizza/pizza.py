from tabulate import tabulate
import csv
import sys

def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        print(f'{read_menu(sys.argv[1])}')

def read_menu(f):
    menu = []
    if(f==f.split(".") or f.split(".")[1]!="csv"):
        sys.exit("Not a CSV file")
    try:
        with open(f) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # O tabulate lê melhor uma lista de dicionários ou listas
                menu.append(row)
        return tabulate(menu, headers="keys", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == "__main__":
    main()
