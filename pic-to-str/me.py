from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

FILE = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

chars = '$ '


def getchar(r, g, b, a=256):
    if a == 0:
        return ' '

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    step = 256 / len(chars)
    return chars[int(gray / step)]


if __name__ == '__main__':
    img = Image.open(FILE)
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    text = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            text += getchar(*img.getpixel((j, i)))
        text += '\n'

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(text)
    else:
        with open('output.txt', 'w') as f:
            f.write(text)