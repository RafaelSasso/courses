def main():
    word = input("Input: ")
    print(f'Output: {shorten(word)}')

def shorten(word):
    vowels = ['a','e','i','o','u']
    temp = ""
    for letter in word:
        if letter.lower() not in vowels:
            temp += letter
    return temp

if __name__ == "__main__":
    main()
