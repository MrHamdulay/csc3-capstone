from algorithms.treehash import TreeHash, PythonProgram
import os
import sys

detectors = [TreeHash]

files = []
if len(sys.argv) > 2:
    files = sys.argv[1:]
elif len(sys.argv) == 2:
    for _, _, given_files in os.walk(sys.argv[1]):
        files += given_files

# filter file types
for f in files:


detector = TreeHash()

programSubmissions = [PythonProgram(open(filename).read(), filename) for filename in sys.argv[1:]]
print 'LISTINGS!'
for program in programSubmissions:
    detector.isPlagiarised(program)

for program in programSubmissions:
    print 'NEW PROGRAM'
    print program.listing
