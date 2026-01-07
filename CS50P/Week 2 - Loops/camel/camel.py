def main():
    camel = input("camelCase: ")
    print(snake(camel))

def snake(camel):
    temp = ""
    for i in range(len(camel)):
        if(camel[i].isupper()):
            temp += "_"
        temp += camel[i]
    return temp.lower()

if __name__ == "__main__":
    main()
