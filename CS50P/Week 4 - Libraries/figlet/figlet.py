from pyfiglet import Figlet
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) > 2:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) > 1:
        sys.exit("Invalid usage")

    s = input("Input: ")

    print(figlet.renderText(s))


main()
