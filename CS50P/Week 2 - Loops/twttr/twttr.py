def main():
    twt = input("Input: ")
    print(f'Output: {twitter(twt)}')

def twitter(txt):
    vowels = ['a','e','i','o','u']
    temp = ""
    for letter in txt:
        if letter.lower() not in vowels:
            temp += letter
    return temp

main()
