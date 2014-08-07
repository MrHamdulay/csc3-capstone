from algorithms.treehash import TreeHash
import sys

detectors = [TreeHash]

if len(sys.argv) < 2:
  print 'python capstone [<file1>.py]'
  sys.exit(1)

detector = TreeHash()

files = [open(filename).read() for filename in sys.argv[1:]]
for file_ in files:
    detector.isPlagiarised(file_)

