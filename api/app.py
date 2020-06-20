from flask import Flask

app = Flask(__name__)


@app.route('/')
def _():
  return 'route'


if __name__ == "__main__":
  app.run()
