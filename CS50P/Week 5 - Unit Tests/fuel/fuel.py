def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass

def gauge(p):
    if p<=1:
        return "E"
    elif p>=99:
        return "F"
    return str(round(p*100))+"%"

def convert(fraction):
    fraction = str(fraction)
    x,y = fraction.split("/")
    if (int(x) < 0 or int(y) < 0) or (int(x)>int(y)):
        raise ValueError
    return int(x)/int(y)*100



if __name__ == "__main__":
    main()

