from cheaters.detector import Detector
from flask import Flask, render_template, request
from flask.ext.classy import FlaskView, route
app = Flask(__name__)

class View(FlaskView):

  '''
  Web form to submit assignments. This is the starting point.
  @GET /
  @render submit.html
  '''
  def index(self):
    return render_template('submit.html')

  '''
  Receive and Process assignments submitted from the web form
  @POST /submit
  @render :)
  '''
  @route('/submit', methods=['POST'])
  def upload_file(self):
    submission = request.files['submission']
    assignment_number = request.form['assignment_number']
    Detector.run(submission, assignment_number)
    return ':)'

if __name__ == '__main__':
  View.register(app)
  app.run(debug=True)
