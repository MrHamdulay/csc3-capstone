#assignment 6 question 3
#vhrjoc001
#counting votes of random inputted parties

print("Independent Electoral Commission\n--------------------------------")
parties=input("Enter the names of parties (terminated by DONE):\n")
partieslist=[] #list of parties created

while parties !="DONE":
    partieslist.append(parties)
    parties=input()

partieslist.sort()   #sort list into alph order 
temp="DONE"         #create a temporary string to equal values in list
print("\nVote counts:")

for parties in partieslist:
    if parties!= temp: # if variable is not the same as temp start counter
        temp=parties
        print(parties,(10-len(parties))*" "," ","- ",partieslist.count(parties),sep="")
        
    

    