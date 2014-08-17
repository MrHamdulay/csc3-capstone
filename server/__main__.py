from flask import Flask
from flask.ext.classy import FlaskView
app = Flask(__name__)


class View(FlaskView):
  def index(self):
    return 'HELLO WORLD'

if __name__ == '__main__':
  View.register(app)
  app.run(debug=True)
