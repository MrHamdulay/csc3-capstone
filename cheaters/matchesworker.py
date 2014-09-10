from time import sleep

from algorithms.grouper import Grouper
from database import DatabaseManager

print 'Running worker'

database = DatabaseManager()
grouper = Grouper()

while True:
    # 1. figure out if there are submissions we haven't processed
    # 2. processs those submissions by grouping all their signatures
    # 3. update matching submissions appropriately (if the number of matches is greater than existing match)
    max_submission_id = database.fetch_max_submission_id() or 0
    max_submission_match_id = database.fetch_max_submission_match_id() or 0


    for submission_id in xrange(max_submission_match_id+1, max_submission_id+1):
        print 'Processing', submission_id
        matching_signatures = database.lookup_matching_signatures(submission_id)
        signatures_by_document = grouper.group_signatures_by_document(matching_signatures)

        other_submission_id = max(signatures_by_document.iteritems(), key=lambda x: len(x[1]))[0]
        database.store_submission_match(submission_id, other_submission_id, len(signatures_by_document[other_submission_id]))

        for other_submission_id, signatures in signatures_by_document.iteritems():
            num_signatures = len(signatures)
            signature_match = database.fetch_submission_match(other_submission_id)

            if signature_match is None:
                continue
            if num_signatures > signature_match.number_signatures_matched:
                database.update_submission_match(
                        signature_match,
                        match_submission_id=other_submission_id,
                        number_signatures_matched=num_signatures)

        print 'done'

    print 'sleeeep'
    sleep(1)

