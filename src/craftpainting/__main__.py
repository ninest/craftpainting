from craftpainting.painting import create_painting
from craftpainting.enlarge import enlarge_image
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('imagepath', help='the input image path')
parser.add_argument('-o', '--outputpath', help='the output image path')
parser.add_argument('-s', '--size', default='1x1', help='the painting output size (ex: 2x1)')
parser.add_argument('-g', '--gray', default=False, action='store_true', help='whether the output painting should be black and white')
parser.add_argument('-r', '--repeat', default=15, type=int, help='how many times multiply the pixels (set to 0 to get a Minecraft texture)')

args = parser.parse_args()

# convert the size from AxB to (A, B)
width = int(args.size.split('x')[0])
height = int(args.size.split('x')[1])

painting = create_painting(args.imagepath, size=(width, height), gray=args.gray)

if args.repeat != 0:
  painting = enlarge_image(painting, repetitions=args.repeat)

if args.outputpath:
  painting.save(args.outputpath)
else:
  painting.show()
