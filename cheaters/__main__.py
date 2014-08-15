from algorithms.treehashalgorithm import TreeHashAlgorithm
from languages.python import PythonProgram
import os
import sys


# parse command line arguments
if len(sys.argv) > 2:
    files = sys.argv[1:]
elif len(sys.argv) == 2:
    for _, _, given_files in os.walk(sys.argv[1]):
        files += given_files

# filter file types


# read in files and parse into our internal representations
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
detector = TreeHashAlgorithm()
# check each file for plagiarism
for program in programSubmissions:
    detector.isPlagiarised(program)

# print sections of code that have been copied / cheated
for i, program in enumerate(programSubmissions):
    print 'NEW PROGRAM'
    print program.listing
