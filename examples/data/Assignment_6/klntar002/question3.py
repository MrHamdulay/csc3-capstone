# tarisai kalinde
# klntar002
# program to count number of votes

print('Independent Electoral Commission')
print('--------------------------------')
party_names= input('Enter the names of parties (terminated by DONE):\n')  # party name input

_array = {}     # accumulation of dictionary

while party_names!='DONE':                                                # for party name to be entered as long as 'DONE' is not entered
   # if loops for adding input into dictionary and counting occurances
    if party_names in _array:
        _array[party_names]+=1
    else:
        _array[party_names]=1
    
        
    party_names=input('')  # continuous input


    
    
x=sorted(_array.items()) # putting dictionary into sorted list
y=[] #empty list for keys
u=[] # empty list for values
#for loop for going thru both lists
for i in x:
    key_=i[0]
    y.append(key_)
    index_=i[1]
    u.append(index_)

#for loop for going thru compiled lists  
print('\nVote counts:')
for i in y:
    
        diff=9-len(i)
        print(i,' '*diff,'-',u[y.index(i)])


        
    
    

