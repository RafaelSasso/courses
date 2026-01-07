def main():
    string = input("Write your formula: \n")
    print(f'{calculate(string):.1f}')

def calculate(string):
    x,y,z = string.split()

    if(y=="/"):
        return int(x)/int(z)
    elif(y=="*"):
        return int(x)*int(z)
    elif(y=="+"):
        return int(x)+int(z)
    else:
        return int(x)-int(z)

main()
