def einstein(mass):
    c = 300000000
    return mass*(c**2)

def main():
    mass = int(input("m: "))
    print(f"E: {einstein(mass)}")

main()
