""" Counting number of votes in an election
Kumaran Reddy
 25 april 2014 """

print('Independent Electoral Commission')
print('--------------------------------')
Parties=[]
Party=input('Enter the names of parties (terminated by DONE):\n')
Parties.append(Party)
while Party!='DONE':
   Party= input()
   Parties.append(Party)

del Parties[len(Parties)-1]
Parties.sort()

Votes=[]
Number=[]
for i in Parties:
   if i in Votes:
      continue
   else:
      Votes.append(i)

    
for i in Votes:
   if i in Parties:
      count=Parties.count(i)
      Number.append(count)
      
print()        
print('Vote counts:')
for i in range(len(Votes)):
   print(Votes[i],(11-len(Votes[i]))*' ','- ',Number[i],sep='')