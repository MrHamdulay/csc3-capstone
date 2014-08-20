#Program to count number of votes
#annika brundyn
#24/04/2014

#print heading
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):\n")

#ask user for input and convert to dictionary to count votes
parties={}                      #create dictionary
name=input("")
while name!="DONE":
    if name in parties:
        parties[name]+=1        #if key in dictionary, add 1 to it's value
    else: 
        parties[name]=1         #else add new key with a value of 1
    name=input("")
 
#count and print number of votes and sort alphabetically
print("Vote counts:")
for name in sorted(parties):
    print(name," "*(11-len(name)),"- ",parties[name],sep="")