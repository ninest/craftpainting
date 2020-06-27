from craftpainting import create_painting, enlarge_image
from PIL import Image

image = Image.open('images/sunset_dense.jpg')
p = create_painting(image)  # create the (super tiny) image
p = enlarge_image(p, repetitions=15)  # enlarge it so it looks better
p.show()
