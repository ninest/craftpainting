# git subtree push --prefix api heroku master
from flask import Flask, render_template, request, send_file
from PIL import Image
import io
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/create_painting', methods=['POST'])
def create():
  print(request.form)
  print(request.files['image'])

  image_from_form = request.files['image']
  image = Image.open(image_from_form)
  # image.show()

  # file object in memory
  bytesio = io.BytesIO()
  image.save(bytesio, 'PNG')

  image_b64 = base64.b64encode(bytesio.getvalue())

  return render_template('created.html', image_b64=image_b64.decode('ascii'))


if __name__ == "__main__":
  app.run(debug=True)
