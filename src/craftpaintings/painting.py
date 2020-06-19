from PIL import Image
import numpy as np


def create_painting(image_path, size, gray=False):
  image = Image.open(image_path)
  image.thumbnail((size, size))

  if gray:
    image = image.convert(mode='L')

  return image
