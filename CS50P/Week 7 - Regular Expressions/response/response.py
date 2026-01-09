from validator_collection import checkers


def main():
    if(validate(input("What's your email address? "))):
        print("Valid")
    else:
        print("Invalid")


def validate(s):
    return checkers.is_email(s)


if __name__ == "__main__":
    main()
