"""this programme calculates the freqency of a word in a given array
quincy cele
21 april 2013"""

print("Independent Electoral Commission")
print("--------------------------------")
party=input("Enter the names of parties (terminated by DONE):\n")
dictionary={}
if party!="DONE":
    dictionary[party]=dictionary.get(party,1)

#enter the amount of strings wanted by the user to be tallied until the user types in DONE
while party!="DONE":
    party=input("")
    if party!="DONE":
            dictionary[party]=dictionary.get(party,0)+1
print()
print("Vote counts:")
 
 #convert the keys of the dictionary to a list   
appex=list(dictionary)

#sort it to default sort ( is aphabetical order)
appex.sort()

for i in appex:
    print(i," "*(9-len(i)),"-",dictionary[i])


    
    
        
    
    

    
        
            
    


