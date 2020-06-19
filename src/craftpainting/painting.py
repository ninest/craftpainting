from PIL import Image


def create_painting(image_path, size, gray=False):
  image = Image.open(image_path)
  image.thumbnail((size, size))

  # black and white images optional
  if gray:
    image = image.convert(mode='L')

  return image
