from time import sleep

from algorithms.grouper import Grouper
from algorithms.suffixtreealgorithm import SuffixTreeAlgorithm
from database import DatabaseManager

print 'Running worker'

database = DatabaseManager()
grouper = Grouper()

def match(submissions):
    print 'Starting suffix matching'
    line_matches = SuffixTreeAlgorithm().calculate_document_similarity(*submissions)
    num_matches = 0
    print line_matches
    for i in (0, 1):
        num = sum(x.match_length for x in line_matches[i])
        num_matches = max(num, num_matches)
    print num_matches
    return line_matches, num_matches


while True:
    # 1. figure out if there are submissions we haven't processed
    # 2. processs those submissions by grouping all their signatures
    # 3. update matching submissions appropriately (if the number of matches is greater than existing match)
    max_submission_id = database.fetch_max_submission_id() or 0
    max_submission_match_id = database.fetch_max_submission_match_id() or 0


    for submission_id in xrange(max_submission_match_id+1, max_submission_id+1):
        print 'Processing', submission_id
        matching_signatures = database.lookup_matching_signatures(submission_id)
        submissions = [database.fetch_a_submission(submission_id)]
        signatures_by_document = grouper.group_signatures_by_document(matching_signatures, False)

        other_submission_id = max(signatures_by_document.iteritems(), key=lambda x: len(x[1]))[0]
        submissions.append(database.fetch_a_submission(other_submission_id))
        print 'Matched to', other_submission_id

        line_matches, num_matches = match(submissions)

        if line_matches[0]:
            database.store_submission_match(submissions[0].assignment_id, submission_id, other_submission_id,  len(signatures_by_document[other_submission_id]), num_matches)
            database.store_matches(submission_id, other_submission_id, line_matches[0], line_matches[1])
        else:
            continue
        print 'done'

        for other_submission_id2, signatures in signatures_by_document.iteritems():
            break
            num_signatures = len(signatures)
            other_submission = database.fetch_a_submission(other_submission_id2)
            signature_match = database.fetch_submission_match(other_submission_id2)

            if signature_match is None:
                continue
            if num_signatures > signature_match.number_signatures_matched:
                line_matches, num_matches = match([submissions[0], other_submission])
                if num_matches > signature_match.confidence:
                    if line_matches[0]:
                        database.store_matches(submission_id, other_submission_id2, line_matches[0], line_matches[1])
                    database.update_submission_match(
                            submission_id,
                            signature_match,
                            match_submission_id=other_submission_id2,
                            confidence=num_matches,
                            number_signatures_matched=num_signatures)

        print 'done'

    print 'sleeeep'
    sleep(1)

