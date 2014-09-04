from flask import Flask, render_template, request, redirect
from flask.ext.classy import FlaskView, route
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from detector import Detector
from database import DatabaseManager
from algorithms.grouper import Grouper

class View(FlaskView):

    @route('/')
    def index_page(self):
        ''' List assignments on the home page
        @GET /
        @render assignments.html
        '''
        database = DatabaseManager()
        assignments = database.fetch_current_assignments()
        return render_template('assignments.html' , assignments=assignments)

    @route('/submit')
    def view_submit_form(self):
        ''' Web form to submit assignments.
        @GET /submit
        @render submit.html
        '''
        database = DatabaseManager()
        assignments = database.fetch_current_assignments()
        return render_template('submit.html', assignments=assignments)

    @route('/submit', methods=['POST'])
    def post_submit_form(self):
        ''' Receive and Process assignments submitted from the web form
        @POST /submit
        @redirect /{assignment_id}
        '''
        submission = request.files['submission']
        assignment_id = request.form['assignment_id']
        Detector().run(submission, assignment_id)
        return redirect('/' + assignment_id)

    @route('/createAssignment')
    def view_create_assignment(self):
        ''' View the Assignment submission form
        @GET /createAssignment
        @render createAssignment.html
        '''
        return render_template('createAssignment.html')

    @route('/createAssignment', methods=['POST'])
    def post_create_assignment(self):
        ''' Create an assignment and persist it to the database
        @POST /createAssignment
        @redirect /
        '''
        detector = Detector()
        courseCode = request.form['courseCode']
        dateDue = request.form['dueDate']
        assignmentDescription = request.form['description']
        detector.runAssignment(assignmentDescription,dateDue,courseCode)
        return redirect('/')

    @route('/<int:assignment_num>')
    def view_submissions(self, assignment_num):
        ''' Lists submissions in a given assignment_num
        @GET /{assignment_num}'
        @render submissions.html'''
        database = DatabaseManager()
        submissions = database.fetch_submissions(assignment_num)
        return render_template('submissions.html',
                submissions=submissions, assignment_num=assignment_num)

    @route('/<int:assignment_num>/<submission_id>')
    def view_diff(self, assignment_num, submission_id):
        ''' View code diffs against the given submission
        @GET /{assignment_num}/{submission_id}
        @render diff.html'''
        database = DatabaseManager()
        submission = database.fetch_a_submission(assignment_num, submission_id)

        signatures = database.lookup_matching_signatures(submission_id)
        groups = Grouper().group(signatures, submission.program_source)
        print '\n'.join(str(x) for x in groups[2])
        # get the submission_id of the group with the most number of matches
        other_submission_id = max(groups.iteritems(), key=lambda x: len(x[1]))[0]
        other_submission = database.fetch_a_submission(assignment_num, other_submission_id)

        submission_match_string = ','.join(
                '%d-%d'%(m.start_line_mine, m.start_line_mine+m.match_length)
                    for m in groups[other_submission_id])
        other_submission_match_string = ','.join(
                '%d-%d'%(m.start_line_mine, m.start_line_mine+m.match_length)
                    for m in groups[other_submission_id])

        return render_template('diff.html',
                submission=submission,
                submission_match_string=submission_match_string,
                other_submission=other_submission,
                other_submission_match_string=other_submission_match_string,
                assignment_num=assignment_num)

if __name__ == '__main__':
    app = Flask(__name__)
    View.register(app)
    app.run(debug=True)
