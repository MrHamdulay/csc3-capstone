"""Print list of political parties with number of votes.
Trevor Byaruhanga
21 April 2014"""



# get a politcal party from user
print('Independent Electoral Commission')
print('--------------------------------')
single=[]
#start with a zero counter
counter = {}

print('Enter the names of parties (terminated by DONE):')
#while logic is false if the items do not exist in the list add them then sort them out alphabetically
logic=False
while logic==False:
    politics=input('')
    
    if politics!='DONE':
        single.append(politics)
        sorted(single)
    elif politics=='DONE':
        logic=True
        break
# once logic is true, print the list of political parties(counter keys) in alphabetical order with how many votes they got(counter values).
if logic==True:
    
    print()
    print('Vote counts:')
    for i in single:
        if not i in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    for i in sorted(counter):
        
        print (i,' '*(10-(len(i)))+'-',counter[i])    


