# git subtree push --prefix api heroku master
from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import base64
from craftpainting.painting import create_painting
from craftpainting.enlarge import enlarge_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/create_painting', methods=['POST'])
def create():
  width = request.form['width']
  height = request.form['height']
  gray = request.form.getlist('bw')
  frame = request.form.getlist('frame')

  # set size
  if not width or not height:
    size = None
  else:
    size = (int(width), int(height))

  if "on" in gray: gray = True
  else: gray = False
  if "on" in frame: frame = True
  else: frame = False

  image_from_form = request.files['image']
  image = Image.open(image_from_form)

  painting = create_painting(image, size=size, gray=gray, border=frame)
  painting = enlarge_image(painting, repetitions=20)

  # file object in memory
  bytesio = io.BytesIO()
  painting.save(bytesio, 'PNG')

  image_b64 = base64.b64encode(bytesio.getvalue())

  return render_template('created.html', image_b64=image_b64.decode('ascii'))


if __name__ == "__main__":
  app.run(debug=True)
