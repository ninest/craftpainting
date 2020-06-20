from craftpainting.painting import create_painting
from craftpainting.enlarge import enlarge_image
from PIL import Image

p = create_painting('images/cat.jpeg')
p = enlarge_image(p, repetitions=20)
p.show()
