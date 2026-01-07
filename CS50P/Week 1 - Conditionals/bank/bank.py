def main():
    i = input("Greetings: ")
    print(f"${bank(i)}")

def bank(ipt):
    ipt = ipt.lower().strip()
    if(ipt.startswith("h")):
        if(ipt.startswith("hello")):
            return 0
        else:
            return 20
    else:
        return 100

main()
