print('Independent Electoral Commission')
print('--------------------------------')
vote = input('Enter the names of parties (terminated by DONE):\n')
vote_list=[]
vote_list.append(vote)

while vote!='DONE':
    vote=input('')
    vote_list.append(vote)
print()
vote_list.remove(vote_list[-1])
vote_list.sort()
party_names=[]
vote_count=[]
count=0
vote_tmp=[]
for i in vote_list:
    if i in party_names:
        continue
    else:
        party_names.append(i)

for j in vote_list:
    count=0
    if j in vote_tmp:
        continue
    for k in vote_list:
        if k==j:
            count+=1
            vote_tmp.append(k)
    vote_count.append(count)
gap=' '
print('Vote counts:')
for i in range (len(party_names)):
    print("{0:<10}".format(party_names[i]),'-',vote_count[i])
   


            
            
   
        

            
        
            
        
    
    
    