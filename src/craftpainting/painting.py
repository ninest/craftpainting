from PIL import Image
import numpy as np
import random
# import requests
from io import BytesIO
# import validators

BLOCK_SIZE = 16

# list of colors for the frame (all browns)
FRAME_COLORS = [
    (67, 61, 49),
    (68, 58, 48)
]


def create_painting(image, size=None, gray=False, border=True):
  # image path can be from internet too
  # if validators.url(image_path):
  #   response = requests.get(image_path)
  #   image = Image.open(BytesIO(response.content))
  # else:
  #   image = Image.open(image_path)

  if size is None:
    # try to detect what the size should be if it's not provided
    image_width, image_height = image.size
    ratio = image_width / image_height

    # print(ratio)

    if ratio > 1.33:
      size = (2, 1)
    elif ratio < 0.76:
      size = (1, 2)
    else:
      size = (1, 1)

  # convert the size from block to pixels
  image_size = size[0] * BLOCK_SIZE, size[1] * BLOCK_SIZE

  # black and white images optional
  if gray:
    image = image.convert(mode='L')

  if border:
    # create a brown image
    parent_image = Image.new('RGB', image_size)

    array = np.array(parent_image)
    for row_index in range(len(array)):
      for col_index in range(len(array[row_index])):
        array[row_index][col_index] = random.choice(FRAME_COLORS)

    parent_image = Image.fromarray(array)

    # adjust the old size
    # reduce it to make space for the frame
    image = image.resize((image_size[0]-2, image_size[1]-2), Image.ANTIALIAS)

    # page the image on the parent_image so it has a border
    parent_image.paste(image, (1, 1))

    # overwrite the original image variable
    image = parent_image

  else:
    # no border, just resize image
    image = image.resize(image_size, Image.ANTIALIAS)

  return image
