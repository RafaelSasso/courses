def main():
    greet = input("Greetings: ")
    print(f"${value(greet)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if(greeting.startswith("h")):
        if(greeting.startswith("hello")):
            return 0
        else:
            return 20
    else:
        return 100


if __name__ == "__main__":
    main()
