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
    def list_diff(self, assignment_num, submission_id):
        database = DatabaseManager() # TODO: do we want to make the databaseManager a class attribute?
        submission = database.fetch_a_submission(assignment_num, submission_id)

        signatures = database.lookup_matching_signatures(submission_id)
        groups = Grouper().group(signatures)
        print '\n'.join(str(x) for x in groups[2])
        # get the submission_id of the group with the most number of matches
        other_submission_id = max(groups.iteritems(), key=lambda x: len(x[1]))[0]
        other_submission = database.fetch_a_submission(assignment_num, other_submission_id)

        submission_match_string = ','.join(
                '%d-%d'%(m.start_line_mine+1, m.start_line_mine+m.match_length+1)
                    for m in groups[other_submission_id])
        other_submission_match_string = ','.join(
                '%d-%d'%(m.start_line_theirs+1, m.start_line_theirs+m.match_length+1)
                    for m in groups[other_submission_id])

        return render_template('diff.html',
                submission=submission,
                submission_match_string=submission_match_string,
                other_submission=other_submission,
                other_submission_match_string=other_submission_match_string,
                assignment_num=assignment_num)

if __name__ == '__main__':
    View.register(app)
    app.run(debug=True)
