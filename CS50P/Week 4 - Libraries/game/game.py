import random

def main():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue

        if(n>0):
            break

    rand = random.randint(1, n)

    while True:
        try:
            g = int(input("Guess: "))
        except ValueError:
            continue

        if(g<=0):
            continue
        if(g<rand):
            print("Too small!")
        elif(g>rand):
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
