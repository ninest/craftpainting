from PIL import Image
import numpy as np

def enlarge_image(image, repetitions=10):
  array = np.array(image)

  # print(array)

  # repeat in both axis
  array = np.repeat(array, repetitions, axis=0)
  array = np.repeat(array, repetitions, axis=1)

  return Image.fromarray(array)