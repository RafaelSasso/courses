def convert(list):
    nstr = ""
    for s in list:
        if(s== ':)' ):
            s="\U0001F642"
        elif(s== ':(' ):
            s="\U0001F641"
        nstr = nstr + " " + s
    return nstr

def main():
    string = input()
    list = string.split()
    result = convert(list)
    print(result.strip())

main()
