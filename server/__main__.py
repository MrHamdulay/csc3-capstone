from flask import Flask, render_template, request
from flask.ext.classy import FlaskView, route
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')

from detector import Detector
from database import DatabaseManager
from algorithms.grouper import Grouper

app = Flask(__name__)

class View(FlaskView):

    '''
    Web form to submit assignments. This is the starting point.
    @GET /submit
    @render submit.html
    '''
    @route('/submit')
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
        assignment_id = request.form['assignment_id']
        Detector().run(submission, assignment_id)
        return ':)'

    '''
    Display results:
        -Assignment
            -List of submissions, e.g. DBRJAR001 (90%)
                - 2 way diffs
    '''
    @route('/')
    def list_assignments(self):
        database = DatabaseManager()
        assignments = database.fetch_current_assignments()
        return render_template('assignments.html' , assignments=assignments)

    @route('/<assignment_num>')
    def list_submissions(self, assignment_num):
        database = DatabaseManager() # TODO: do we want to make the databaseManager a class attribute?
        submissions = database.fetch_submissions(assignment_num)
        return render_template('submissions.html',
                submissions=submissions, assignment_num=assignment_num)

    @route('/<assignment_num>/<submission_id>')
    def list_of_submissions(self, assignment_num, submission_id):
        database = DatabaseManager() # TODO: do we want to make the databaseManager a class attribute?
        submission = database.fetch_a_submission(assignment_num, submission_id)
        groups = Grouper().group(signatures)
        return render_template('submission.html',
                submission=submission, assignment_num=assignment_num)

if __name__ == '__main__':
    View.register(app)
    app.run(debug=True)
