from algorithms.treehash import TreeHash, PythonProgram
import os
import sys

detectors = [TreeHash]

if len(sys.argv) > 2:
    files = sys.argv[1:]
elif len(sys.argv) == 2:
    for _, _, given_files in os.walk(sys.argv[1]):
        files += given_files

# filter file types


programSubmissions = []
for filename in files:
  try:
    programSubmissions.append(PythonProgram(open(filename).read(), filename))
  except SyntaxError as e:
    print 'Syntax error in ', filename
    print e
    sys.exit(1)

print programSubmissions

print 'LISTINGS!'
detector = TreeHash()
for program in programSubmissions:
    detector.isPlagiarised(program)

for program in programSubmissions:
    print 'NEW PROGRAM'
    print program.listing
