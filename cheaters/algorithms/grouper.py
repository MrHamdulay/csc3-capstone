from collections import defaultdict
from model.match import Match

MIN_MATCH_LENGTH = 3

''' Given a list of signatures find patterns and groups of common code '''
class Grouper:
    def group(self, signatures, program_source):
        ''' given a list of signatures group and return a list of matches '''
        program_source = program_source.split('\n')

        # first group by document
        group_by_document = defaultdict(list)
        for signature in signatures:
            group_by_document[signature.submission_id_theirs].append(signature)

        document_matches = defaultdict(list)

        # find consecutive matches
        for submission_id, document_signatures in group_by_document.iteritems():
            # sort by line number
            document_signatures.sort(key=lambda x: x.line_number_mine)
            print submission_id, document_signatures
            print ' '.join(str(s.line_number_mine) for s in document_signatures)
            print ' '.join(str(s.line_number_theirs) for s in document_signatures)

            run_start = 0
            last_line = 0
            for i, signature in enumerate(document_signatures):

                # if we no longer matching consecutive signatures
                if signature.line_number_mine - last_line > 1 and i - run_start > 3:
                    start_signature = document_signatures[run_start]
                    match = Match(submission_id,
                                  start_signature.line_number_mine,
                                  start_signature.line_number_theirs,
                                  signature.line_number_mine - start_signature.line_number_mine,
                                  i - run_start)
                    document_matches[submission_id].append(match)
                    run_start = i

                last_line = signature.line_number_mine
                # we are nice and ignore empty lines for signatures
                while program_source[last_line].strip() == '':
                    last_line += 1

        return document_matches
