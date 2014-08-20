"""question 3-assignment 6- party votes
GVNPRI022
23 April 2014"""
print("Independent Electoral Commission")
print("--------------------------------")
partyVar=input(("Enter the names of parties (terminated by DONE):\n\n"))
x=0
check="true"
counter=[[]]
if(partyVar!="DONE"):
    counter=[[partyVar,0]]
else:
    check="false"
found=-1
while(partyVar!="DONE"):   #end loop when 'DONE' entered
    
    for i in range (len(counter)):
        if (partyVar==counter[i][0]): #adding vote if party in array
            counter[i][1]= counter[i][1]+1
            found=0
            
    if (found ==-1): #adding new party to array
        
        counter.append([partyVar,1])
    found=-1
    partyVar=input()   

counter.sort() #sorting array
print("Vote counts:")
if (check=="true"):
    
    for k in range (len(counter)): #formatting and displaying
        s= "{0:<11}- {1}"
        print(s.format(counter[k][0],counter[k][1]))
    
            
