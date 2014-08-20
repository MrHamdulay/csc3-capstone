"""Right alligne a list of words with the longest words
B.Player
20/04/2014"""

#initialising variables
parties={}
word=''

#printing headers
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

#adding party names to dictionery + adding up votes
while True:
      word = input()
      if word!='DONE':
            if word in parties:
                  parties[word]+=1
            else: 
                  parties[word]=1
      else: break

#outputing sorted list 
print("\nVote counts:")
for party in sorted(parties):
      form="{0:<10} - {1}"
      print(form.format(party,parties[party]))
   
