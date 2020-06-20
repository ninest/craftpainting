from craftpainting.painting import create_painting
from craftpainting.enlarge import enlarge_image
from PIL import Image

image = Image.open('images/cat.jpeg')
p = create_painting(image)
p = enlarge_image(p, repetitions=20)
p.show()
