from PIL import Image
import numpy as np
import random

BLOCK_SIZE = 16

# list of colors for the frame (all browns)
FRAME_COLORS = [
    # (44, 38, 32),
    (67, 61, 49),
    (68, 58, 48)
]


def create_painting(image_path, size, gray=False, border=False):
  image = Image.open(image_path)

  if border:
    # create a brown image
    parent_image = Image.new('RGB', size)

    array = np.array(parent_image)
    for row_index in range(len(array)):
      for col_index in range(len(array[row_index])):
        array[row_index][col_index] = random.choice(FRAME_COLORS)

    parent_image = Image.fromarray(array)

    # adjust the old size
    image = image.resize((size[0]-2, size[1]-2), Image.ANTIALIAS)

    # page the image on the parent_image so it has a border
    parent_image.paste(image, (1, 1))

    # overwrite the original image variable
    image = parent_image

  else:
    image = image.resize(size, Image.ANTIALIAS)

  # black and white images optional
  if gray:
    image = image.convert(mode='L')

  return image
