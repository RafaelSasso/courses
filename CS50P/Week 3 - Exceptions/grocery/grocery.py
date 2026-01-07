def main():
    d = {}
    while True:
        try:
            item = input()
            if (item == ""):
                continue
            else:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1

        except EOFError:
            print()
            break

    d = dict(sorted(d.items()))
    for i in d:
        print(d[i], i.upper())

main()
