def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(len(s)>6 or len(s)<2):
        return False

    if(not s[:2].isalpha()):
        return False

    for i in range(len(s)):
        if(not s[i].isalnum() or s[i].isspace()):
            return False

        if(i>0):
            if(not s[i].isnumeric() and s[i-1].isnumeric()):
                return False
            if(s[i]=="0" and not s[i-1].isnumeric()):
                return False

    return True

if __name__ == "__main__":
    main()
