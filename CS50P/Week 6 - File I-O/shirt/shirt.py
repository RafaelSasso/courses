# I tried everything using Image only, but resize would simply
# reshape the initial image completely, so i researched a bit
# and came across this ImageOps to make one image fit into another

from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        converter(sys.argv[1], sys.argv[2])

def converter(op, save):
    ext = save.rsplit(".", 1)[-1].lower()

    if ext not in ("png", "jpg", "jpeg"):
        sys.exit("Invalid output")

    if not (op.split(".")[1] == save.split(".")[1]):
        sys.exit("Input and output have different extensions")

    try:
        photo = Image.open(op)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(save)

if __name__ == "__main__":
    main()
