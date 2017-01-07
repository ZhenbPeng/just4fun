# coding: utf-8
import argparse
from PIL import Image

def jpg2txt(filename, maxLen=80, output_file='jpg2txt.txt'):

    try:
        maxLen = int(maxLen)
    except:
        maxLen = 80

    chs = "MNHQ$OC?7>!:-;. "

    try:
        img = Image.open(filename)
    except IOError:
        exit("file not found:{}".format(filename))

    width, height = img.size
    rate = float(maxLen) / max(width, height)
    width = int(rate * width)
    height = int(rate * height)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)

    try:
        im = Image.new('RGB', img.size)
        im.paste(img)
        im = im.resize((width, height))
        string = ''
        for h in range(height):
            for w in range(width):
                rgb = im.getpixel((w, h))
                string += chs[int(sum(rgb) / 3.0 / 256.0 * 16)]
            string += '\n'
        img.seek(img.tell() + 1)
    except EOFError:
        pass

    with open(output_file, 'w') as out_f:
        out_f.write(string)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='jpg input file')
    parser.add_argument('-m', '--maxLen', type=int, help='max width of the output txt')
    parser.add_argument('-o', '--output', help='name of the output file')
    args = parser.parse_args()

    jpg2txt(args.filename, maxLen=args.maxLen, output_file=args.output)

if __name__ == '__main__':
    main()