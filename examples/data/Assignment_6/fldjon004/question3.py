#jono field
#24 april 2014
#question 3


print("Independent Electoral Commission")
print("--------------------------------")
partyname = input("Enter the names of parties (terminated by DONE):\n")
D={}
while partyname != "DONE": #sentinel loop is created
    if partyname not in D: #if not in dictionary already, add to dictionary
        D[partyname] = 1
    else: 
        D[partyname]= D[partyname] + 1
    partyname = input()
    
Mylist = [] 
#coverts dictionary into list

for j in D:
    Mylist.append(j) #adds to list
    
Mylist.sort() #puts list in alphabetical order
print()
print("Vote counts:")

for j in Mylist:
    print(j, " "*(12-len(j)-len(str(D[j]))), "- ", D[j],sep = "")
    
    
    


    