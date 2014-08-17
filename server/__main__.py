import zipfile
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
  @return TODO: complete this
  '''
  @route('/submit', methods=['POST'])
  def upload_file(self):
    submission = request.files['submission']
    assignment_number = request.form['assignment_number']
    Detector.run(assignment_number, submission)
    return ':)'

  '''
  parses the submitted zip archive file
  @param String archive, provided by form POST body
  '''
  def parse_archive(self, archive):
    zf = zipfile.ZipFile(archive)
    files = []
    for info in zf.infolist():
      files.append(self.get_filename(info.filename))
    return files

  '''
  Extracts the file name from the path listed out the zip archive
  'stntnm001/**/filename.py' -> 'filename.py'
  @param String path
  @return String
  '''
  def get_filename(self, path):
    return path.split('/')[-1]

  '''
  Extracts the student number from the submitted file name
  '''
  def get_student_number(self, path):
    return path.split('.')[0]

if __name__ == '__main__':
  View.register(app)
  app.run(debug=True)
