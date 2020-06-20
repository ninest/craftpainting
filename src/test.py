from craftpainting.painting import create_painting
from craftpainting.enlarge import enlarge_image
from PIL import Image

p = create_painting('images/cat.jpeg')
p = enlarge_image(p, repetitions=20)
p.show()
# import numpy as np

# a = np.array([
#   [1,2,3],
#   [4,5,6],
#   [7,8,9],
# ])

# a = np.repeat(a, 10, axis=0)
# a = np.repeat(a, 10, axis=1)
# print(a)