#program to count the number of votes for each political party in an election.
# romelon chetty
# 21 april 2014

print('Independent Electoral Commission')
print('--------------------------------')
parties=[]
party=input('Enter the names of parties (terminated by DONE):\n')
parties.append(party)
while party!='DONE':
   party= input()
   parties.append(party)

del parties[len(parties)-1]
parties.sort()

keys=[]
value=[]
for i in parties:
   if i in keys:
      continue
   else:
      keys.append(i)

    
for i in keys:
   if i in parties:
      count=parties.count(i)
      value.append(count)
      
print()        
print('Vote counts:')
for i in range(len(keys)):
   print(keys[i],(11-len(keys[i]))*' ','- ',value[i],sep='')