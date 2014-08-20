""" Yonela Ford
Counting votes for parties
23 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
x= input("Enter the names of parties (terminated by DONE):\n")
parties=[]

# CREATE LIST OF PARTY
while x!="DONE":
    parties.append(x)
    x=input("")
#CREATE DICTIONARY
counter={}
#GO THROUGH DICTIONARY AND COUNT EACH WORD AND REPITIONS
for i in parties:
    if not i in counter:
        counter[i]=1
    else:
        counter[i]+=1

 #PRINT ALIGNED 
print ()
print("Vote counts:")
for i in sorted(counter.keys()):
    print(i.ljust(10),"-",(counter[i]))
 