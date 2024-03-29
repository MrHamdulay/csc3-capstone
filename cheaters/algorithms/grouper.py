'''
Author: Yaseen Hamdulay, Jarred de Beer, Merishka Lalla
Date: 15 August 2014


Takes signatures from output of winnower algorithm and manipulates them
in various ways.

Grouping by original document, filtering out lonely signatures (signatures
that are multiple lines away from other signatures) and groping consecutive
multi line occurences of signatures into one Match object
'''

from collections import defaultdict
from model.match import Match

''' Given a list of signatures find patterns and groups of common code '''
class Grouper:
    def group_signatures_by_document(self, signatures, sort=True):
        group_by_document = defaultdict(list)
        for signature in signatures:
            assert signature.submission_id_theirs is not None
            group_by_document[signature.submission_id_theirs].append(signature)

        if sort:
            for key in group_by_document:
                # sort by line number
                group_by_document[key].sort(key=lambda x: x.line_number_mine)
        return group_by_document

    def find_document_matches(self, submission_id, document_signatures, program_source):
        # precondition: all signatures need to come from the same document

        document_matches = []

        run_start = 0
        last_line = 0
        for i, signature in enumerate(document_signatures):

            # if we no longer matching consecutive signatures
            if signature.line_number_mine - last_line > 1 :
                start_signature = document_signatures[run_start]
                number_of_signatures = i - run_start
                number_of_expected_lines = signature.line_number_mine - start_signature.line_number_mine
                # don't count blank lines
                number_of_lines = 0
                for line_number in xrange(start_signature.line_number_mine, signature.line_number_mine):
                    if program_source[line_number].strip() != '':
                        number_of_lines += 1

                density = 0 if number_of_lines == 0 else float(number_of_signatures) / number_of_lines
                match = Match(submission_id,
                              start_signature.line_number_mine,
                              signature.line_number_mine - start_signature.line_number_mine,
                              i - run_start)
                # if more than a few matches
                if number_of_lines > 2:
                    document_matches.append(match)
                run_start = i

            last_line = signature.line_number_mine
            # we are nice and ignore empty lines for signatures
            while last_line < len(program_source)-1 and program_source[last_line].strip() == '':
                last_line += 1

        return document_matches

    def group(self, signatures, program_source):
        ''' given a list of signatures group and return a list of matches '''
        program_source = program_source.split('\n')

        group_by_document = self.group_signatures_by_document(signatures)

        document_matches = {}

        # find consecutive matches
        for submission_id, document_signatures in group_by_document.iteritems():
            document_matches[submission_id] = self.find_document_matches(submission_id, document_signatures, program_source)

        return document_matches, group_by_document
