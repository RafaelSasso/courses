import emoji

def main():
    s = input("Input: ")
    emj = emoji.emojize(s)
    if emj == s:
        emj = emoji.emojize(s, language="alias")
    print(f'Output: {emj}')

main()
