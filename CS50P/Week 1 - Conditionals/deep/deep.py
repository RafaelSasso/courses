def main():
    i = input("Deep Thought: ")
    i = i.lower().strip()
    sout = False
    if(i=="42"):
        sout = True
    else:
        if(i == "forty two" or i=="forty-two"):
            sout = True

    if(sout):
        print("Yes")
    else:
        print("No")

main()
