from craftpainting.painting import create_painting
from craftpainting.enlarge import enlarge_image
from PIL import Image
import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('imagepath', help='the input image path')
  parser.add_argument('-o', '--outputpath', help='the output image path')
  parser.add_argument('-s', '--size', default=None, help='the painting output size (ex: 2x1)')
  parser.add_argument('-g', '--gray', default=False, action='store_true', help='whether the output painting should be black and white')
  parser.add_argument('-r', '--repeat', default=15, type=int, help='how many times multiply the pixels (set to 0 to get a Minecraft texture)')

  args = parser.parse_args()

  if args.size is not None:
    # convert the size from AxB to (A, B)
    width = int(args.size.split('x')[0])
    height = int(args.size.split('x')[1])
    size = (width, height)
  else:
    size = None

  image = Image.open(args.imagepath)
  painting = create_painting(image, size=size, gray=args.gray)

  if args.repeat != 0:
    # repeat = 0 means that the image should be its original size (just like actual minecraft textures)
    painting = enlarge_image(painting, repetitions=args.repeat)

  if args.outputpath:
    # only save the image if an output path is specified
    painting.save(args.outputpath)
  else:
    # otherwise just diplay theimage
    painting.show()


if __name__ == "__main__":
  main()
