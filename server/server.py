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
        student_number = request.form['student_number']
        if not student_number:
            student_number = submission.filename
        assignment_id = request.form['assignment_id']
        Detector().run(submission, assignment_id, student_number)
        return redirect('/' + assignment_id)

    @route('/createAssignment')
    def view_create_assignment(self):
        ''' View the Assignment submission form
        @GET /createAssignment
        @render createAssignment.html
        '''
        return render_template('createAssignment.html')

    @route('/deleteAssignment')
    def view_deleteAssignment(self):
        return render_template('deleteAssignment.html')

    @route('/deleteAssignment', methods = ['POST'])
    def delete_assignment(self):
        detector = Detector()
        assignment_number = request.form['assignmentNumber']
        detector.delete_assignment(assignment_number)
        return redirect('/')

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
        submissions = database.fetch_a_submissions(assignment_num)
        return render_template('submissions.html',
                submissions=submissions, assignment_num=assignment_num)

    @route('/<int:assignment_num>/<submission_id>/new')
    def new_view_diff(self, assignment_num, submission_id):
        database = DatabaseManager()
        submission = database.fetch_a_submission(assignment_num, submission_id)
        other_submission = Detector.find_most_similar_submission(submission)

        Detector.calculate_document_similarity(submission, other_submission)

        return 'workish'

    @route('/<int:assignment_num>/<submission_id>')
    def view_diff(self, assignment_num, submission_id):
        ''' View code diffs against the given submission
        @GET /{assignment_num}/{submission_id}
        @render diff.html'''
        database = DatabaseManager()
        submission = database.fetch_a_submission(assignment_num, submission_id)

        signatures = database.lookup_matching_signatures(submission_id)
        groups, left_group = Grouper().group(signatures, submission.program_source)

        # get the submission_id of the group with the most number of matches
        other_submission_id = max(groups.iteritems(), key=lambda x: len(x[1]))[0]
        other_submission = database.fetch_a_submission(assignment_num, other_submission_id)

        inverted_signatures = map(lambda x: x.reverse(), left_group[other_submission_id])
        inverted_groups, right_group_groups = Grouper().group(inverted_signatures, other_submission.program_source)

        # print signature densities
        left_group = left_group[other_submission_id]
        left_group_counts = [0]*len(submission.program_source)
        right_group = right_group_groups[int(submission_id)]
        right_group_counts = [0]*len(other_submission.program_source)
        for s in left_group:
            left_group_counts[s.line_number_mine] += 1
        for s in right_group:
            right_group_counts[s.line_number_mine] += 1
        # add signature densities to program source
        submission.program_source = '\n'.join('%.2d: %s' % (left_group_counts[i], line) for i, line in enumerate(submission.program_source.split('\n')))
        other_submission.program_source = '\n'.join('%.2d: %s' % (right_group_counts[i], line) for i, line in enumerate(other_submission.program_source.split('\n')))



        submission_match_string = ','.join(
                '%d-%d'%(m.start_line_mine, m.start_line_mine+m.match_length)
                    for m in groups[other_submission_id])
        other_submission_match_string = ','.join(
                '%d-%d'%(m.start_line_mine, m.start_line_mine+m.match_length)
                    for m in inverted_groups[int(submission_id)])

        return render_template('diff.html',
                submission=submission,
                submission_match_string=submission_match_string,
                other_submission=other_submission,
                other_submission_match_string=other_submission_match_string,
                assignment_num=assignment_num)

    @route('/test/<int:assignment_num>/<submission_id>')
    def test_diff(self, assignment_num, submission_id):
        database = DatabaseManager()
        submission = database.fetch_a_submission(assignment_num, submission_id)

        signatures = database.lookup_matching_signatures(submission_id)

        # first group by document
        from collections import defaultdict
        group_by_document = defaultdict(list)
        for signature in signatures:
            group_by_document[signature.submission_id_theirs].append(signature)

        document_matches = defaultdict(list)

        result = ''

        # find consecutive matches
        for submission_id, document_signatures in group_by_document.iteritems():
            # sort by line number
            document_signatures.sort(key=lambda x: x.line_number_mine)
            result += '<h1>%s</h1><pre>' % str(submission_id)
            for s in document_signatures:
                result += '%s %s %s\n' % (s.ngram_hash.ljust(10), str(s.line_number_mine).ljust(10), str(s.line_number_theirs))
            result += '</pre>'


        return result


if __name__ == '__main__':
    app = Flask(__name__)
    View.register(app)
    app.run(debug=True)
