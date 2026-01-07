def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x,y = fraction.split("/")
            output = percentage(int(x),int(y))
            if (int(x) < 0 or int(y) < 0) or (int(x)>int(y)):
                raise ValueError
            print(output)
            break
        except (ValueError, ZeroDivisionError):
            pass

def percentage(x, y):
    p = x/y
    if p<=0.01:
        return "E"
    elif p>=0.99:
        return "F"
    return str(round(p*100))+"%"

main()
