from flask import Flask, render_template, request
from flask.ext.classy import FlaskView, route
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')

from detector import Detector
from database import DatabaseManager

app = Flask(__name__)

class View(FlaskView):

    '''
    Web form to submit assignments. This is the starting point.
    @GET /
    @render submit.html
    '''
    @route('/')
    def index(self):
        database = DatabaseManager()
        assignments = database.fetch_current_assignments()

        return render_template('submit.html', assignments=assignments)

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

    '''
    Display results:
        -Assignment
            -List of submissions, e.g. DBRJAR001 (90%)
                - 2 way diffs
    '''
    @route('/assignments')
    def list_of_assignments(self):
        # TODO: get assignments from db
        # TODO: return template
        return ':]'

    @route('/assignments/<assignment_id>')
    def assignment(self, assignment_id, submission_id):
        # TODO: get results from db
        # TODO: return template
        return ':D'

    @route('/assignments/<assignment_id>/<submission_id>')
    def list_of_submissions(self, id):
        # TODO: get results from db
        # TODO: return template
        return 'XD'

if __name__ == '__main__':
    View.register(app)
    app.run(debug=True)
