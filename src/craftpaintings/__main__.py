from craftpaintings.painting import create_painting
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('imagepath', help='specify the input image path')
parser.add_argument('--size', default=10, help='the painting output size')
parser.add_argument('--gray', default=False, action='store_true', help='true/false depending on whether the output painting should be black and white')

args = parser.parse_args()
print(args)

painting = create_painting(args.imagepath, size=int(args.size), gray=args.gray)
painting.show()
