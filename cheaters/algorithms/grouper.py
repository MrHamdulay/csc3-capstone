from collections import defaultdict
from model.match import Match

MIN_MATCH_LENGTH = 3

''' Given a list of signatures find patterns and groups of common code '''
class Grouper:
    def group(self, signatures):
        ''' given a list of signatures group and return a list of matches '''

        # first group by document
        group_by_document = defaultdict(list)
        for signature in signatures:
            group_by_document[signature.submission_id_theirs].append(signature)

        document_matches = defaultdict(list)

        # find consecutive matches
        for submission_id, document_signatures in group_by_document.iteritems():
            # sort by line number
            document_signatures.sort(key=lambda x: x.line_number_mine)

            current_signature_run = 0
            current_line = document_signatures[0].line_number_mine
            start_line_mine = document_signatures[0].line_number_mine
            start_line_theirs = document_signatures[0].line_number_theirs


            for signature in document_signatures:
                if signature.line_number_mine - current_line <= 1:
                    current_signature_run += 1
                    current_line = signature.line_number_mine
                else:
                    if current_line - start_line_mine >= MIN_MATCH_LENGTH:
                        match = Match(submission_id,
                                      start_line_mine,
                                      start_line_theirs,
                                      current_line - start_line_mine,
                                      current_signature_run)
                        document_matches[submission_id].append(match)

                    # reset everything
                    current_line_run = 0
                    current_signature_run = 0
                    current_line = signature.line_number_mine
                    start_line_mine = signature.line_number_mine
                    start_line_theirs = signature.line_number_theirs

        return document_matches
