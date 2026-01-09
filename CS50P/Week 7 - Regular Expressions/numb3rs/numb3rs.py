import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^([1-9]{1}[0-9]{0,2})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"

    matches = re.search(pattern, ip)
    if matches:
        for group in matches.groups():
            if int(group)>255:
                return False
    return bool(matches)

if __name__ == "__main__":
    main()
