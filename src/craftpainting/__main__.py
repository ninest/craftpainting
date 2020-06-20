from craftpainting.painting import create_painting
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('imagepath', help='the input image path')
parser.add_argument('-o', '--outputpath', help='the output image path')
parser.add_argument('-s', '--size', default=16, help='the painting output size')
parser.add_argument('-g', '--gray', default=False, action='store_true', help='whether the output painting should be black and white')

args = parser.parse_args()

painting = create_painting(args.imagepath, size=int(args.size), gray=args.gray)

if args.outputpath:
  painting.save(args.outputpath)
else:
  painting.show()
