import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../cheaters')
from languages.python import PythonLanguageHandler

code = '''
""" Program to printout names of parties and their vote counts
Mazwi Myeza
21 April 2014
Assignment6
Question3
"""
#Creating arrays and printing heading
votes = []
parties = []
partyVotes = []
print("Independent Electoral Commission")
print("--------------------------------")
#Asking user for input and storing it in the created array
vote = input("Enter the names of parties (terminated by DONE):\\n")
counter = 0
while vote != 'DONE':
    votes.append(vote)
    counter += 1
    vote = input()
#sorting votes
votes.sort()
#populating an array for the parties voted for
for i in range(counter):
    if votes[i] in parties:
        None
    else:
        parties.append(votes[i])
#populating an array for the number of votes a party has recieved
count = 0
for j in range(len(parties)):
    count = votes.count(parties[j])
    partyVotes.append(count)
print()
print("Vote counts:")
#printing results in the proper format
for k in range(len(parties)):
    f = "{0:<11}".format(parties[k])
    print(f, partyVotes[k], sep ="- ")
'''

expected=''''s'






i = []
i = []
i = []
i('s')
i('s')

i = i('s')
i = 0
while (i != 's'):
i.a(i)
i += 1
i = i()

i.a()

for i in i(i):
if (i[i] in i):
i    else:

i.a(i[i])

i = 0
for i in i(i(i)):
i = i.a(i[i])
i.a(i)
i()
i('s')

for i in i(i(i)):
i = 's'.a(i[i])
i(i, i[i], k='s')'''

class PythonCanonicalisationTest(unittest.TestCase):

    def test_renamer_transform(self):
        # not sure how to test
        return

    def test_python_language_handler(self):
        py_language_handler = PythonLanguageHandler()
        py_language_handler.parse_file(code)
        source = py_language_handler.strip_unstable_atrributes(False)
        self.assertEqual(source.strip(), expected.strip())



if __name__ == '__main__':
    unittest.main()
