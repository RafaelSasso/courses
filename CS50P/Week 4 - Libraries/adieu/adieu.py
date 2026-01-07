import inflect

def main():
    p = inflect.engine()
    strings=[]
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            break

        if len(strings)==0:
            name = "to " + name

        strings.append(name)

    print("Adieu, adieu, "+ p.join(strings))

main()
