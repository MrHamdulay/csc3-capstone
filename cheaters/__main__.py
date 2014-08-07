from algorithms.treehash import TreeHash
import sys

detectors = [TreeHash]

if len(sys.argv) < 2:
  print 'python capstone [<file1>.py]'
  sys.exit(1)


files = [open(filename).read() for filename in sys.argv[1:]]
map(TreeHash().isPlagiarised, files)
