import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe[^>]*src=["\']?https?://(?:www\.)?youtube\.com/embed/([\w-]+)'
    if matches := re.search(pattern, s):
        link = "https://youtu.be/"+matches.group(1)
        return link


if __name__ == "__main__":
    main()