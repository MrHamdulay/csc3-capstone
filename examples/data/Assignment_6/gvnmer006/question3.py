"""this programme calculates the freqency of a word in a given array
Merosha Govender
GVNMER006
21 april 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
party=input("Enter the names of parties (terminated by DONE):\n")
dictionary={}
if party!="DONE":
    dictionary[party]=dictionary.get(party,1)

#number of strings entered by user will be tallied until user types DONE
while party!="DONE":
    party=input("")
    if party!="DONE":
            dictionary[party]=dictionary.get(party,0)+1
print()
print("Vote counts:")
 
 #keys in the dictionary converted to a list   
appex=list(dictionary)

#default sort ( in aphabetical order)
appex.sort()

for i in appex:
    print(i," "*(9-len(i)),"-",dictionary[i])