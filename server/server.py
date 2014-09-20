from flask import Flask, render_template, request, redirect, jsonify, flash
from flask.ext.classy import FlaskView, route
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../external')
from detector import Detector
from database import DatabaseManager
from algorithms.grouper import Grouper
from algorithms.suffixtreealgorithm import SuffixTreeAlgorithm

class View(FlaskView):

    @route('/')
    def index_page(self):
        ''' List assignments on the home page
        @GET /
        @render home.html
        '''
        database = DatabaseManager()
        assignments = database.fetch_current_assignments()
        return render_template('home.html' , assignments=assignments)

    @route('/student/submit')
    def view_submit_form(self):
        ''' Web form to submit assignments.
        @GET /submit
        @render student_submit.html
        '''
        return render_template('student_submit.html')

    @route('/student/submit', methods=['POST'])
    def post_submit_form(self):
        ''' Receive and Process assignments submitted from the web form
        @POST /submit
        @redirect /{assignment_id}
        '''
        submission = request.files['submission']
        assignment_id = request.form['assignment_id']
        student_number = request.form['student_number']
        if not student_number:
            student_number = submission.filename
        Detector().run(submission, assignment_id, student_number)
        return redirect('/' + assignment_id)

    @route('/assignments/create')
    def view_create_assignment(self):
        ''' View the Assignment submission form
        @GET /assignment/create
        @render assignment_create.html
        '''
        return render_template('assignment_create.html')

    @route('/assignments/create', methods=['POST'])
    def post_create_assignment(self):
        ''' Create an assignment and persist it to the database
        @POST /assignment/create
        @redirect /
        '''
        detector = Detector()
        courseCode = request.form['courseCode']
        dueDate = request.form['dueDate']
        assignmentDescription = request.form['description']
        detector.runAssignment(assignmentDescription,dueDate,courseCode)
        flash('Assignment created.', 'success')
        return redirect('/assignments/manage')

    @route('/assignments/manage')
    def view_manage_assignments(self):
        ''' Update assignment details
        @GET /assignments_edit
        @render assignments_edit.html
        '''
        database = DatabaseManager()
        assignments = database.fetch_current_assignments()
        return render_template('assignments_manage.html', assignments=assignments)

    @route('/assignments/manage', methods=['POST'])
    def manage_assignments(self):
        ''' Either delete or update an assignment
        @OPTIONS
        @redirect / OR @redirect /assignment_edit
        '''
        assignment_num = request.form['assignmentNumber']
        database = DatabaseManager()

        if (request.form['submitBtn'] == 'Edit Selected'):
            return redirect('/assignments/edit/' + assignment_num)

        elif (request.form['submitBtn'] == 'Delete Selected'):
            database.delete_assignment(assignment_num)
            flash('Assignment ' + assignment_num + ' deleted.', 'success')
            return redirect('/assignments/manage')

        flash('Please select an Assignment', 'warning')
        return redirect('/assignments/manage')

    @route('/assignments/edit/<int:assignment_num>')
    def view_edit_assignment(self, assignment_num):
        ''' Edit assignment form
        @GET /assignments/edit/<int:assignment_num>
        @redirect /assignments/edit
        '''
        database = DatabaseManager()
        a = database.fetch_an_assignment(assignment_num)
        return render_template('assignment_edit.html', assignment=a)

    @route('/assignments/edit/<int:assignment_num>', methods=['POST'])
    def update_assignment(self, assignment_num):
        ''' Update assignment
        @PUT /assignments/edit/<int:assignment_num>
        @redirect /assignments/edit
        '''
        database = DatabaseManager()
        courseCode = request.form['courseCode']
        dueDate = request.form['dueDate']
        assignmentDescription = request.form['description']
        database.update_assignment(assignment_num, courseCode, assignmentDescription, dueDate)
        flash('Assignment ' + str(assignment_num) + ' updated.', 'success')
        return redirect('/assignments/manage')

    @route('/cheaters/<int:assignment_num>')
    def view_submissions(self, assignment_num):
        ''' Lists submissions in a given assignment_num
        @GET /{assignment_num}'
        @render cheaters_review.html'''
        database = DatabaseManager()
        submissions = database.fetch_submissions(assignment_num)
        assignments = database.fetch_current_assignments()
        return render_template('cheaters_review.html',
                submissions=submissions, assignment_num=assignment_num, assignments=assignments)


    # AJAX Requests

    @route('/api/<int:assignment_num>/code')
    def json_assignment_code(self, assignment_num):
        ''' Retrieves all the code submitted for a given assignment as JSON
        @GET /{assignment_num}/code
        @render JSON'''
        database = DatabaseManager()
        source_codes = database.fetch_source_codes(assignment_num)
        return jsonify(**source_codes)

    @route('/api/<int:assignment_num>/matches')
    def json_assignment_matches(self, assignment_num):
        database = DatabaseManager()
        matches = [x.apiify() for x in database.fetch_all_submission_matches(assignment_num)]
        return jsonify({'matches': matches})

    @route('/api/<int:assignment_num>/<int:submission_id>/')
    def json_submission_match_numbers(self, assignment_num, submission_id):
        database = DatabaseManager()
        submission = database.fetch_a_submission(assignment_num, submission_id)
        other_submission = Detector.find_most_similar_submission(submission)

        submission_matches = SuffixTreeAlgorithm().calculate_document_similarity(submission, other_submission)

        match_strings = []
        for matches in submission_matches:
            match_string = ','.join(
                    '%d-%d'%(m.start_line_mine+1, m.start_line_mine+m.match_length+1)
                        for m in matches)
            match_strings.append(match_string)
        return jsonify(source=match_strings[0], target=match_strings[1])


if __name__ == '__main__':
    app = Flask(__name__)
    View.register(app)
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True)
