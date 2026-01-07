import csv
import sys


def main():
    if len(sys.argv)==1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        read(sys.argv[1], sys.argv[2])

def read(read, write):
    students=[]
    try:
        with open(read) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(",")
                students.append({"first":first.strip(), "last":last.strip(), "house":row["house"]})
    except FileNotFoundError:
        sys.exit("File not found")

    #   students = sorted(students, key=lambda student: student["first"])

    with open(write, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first":student["first"], "last":student["last"], "house":student["house"]})

if __name__ == "__main__":
    main()
