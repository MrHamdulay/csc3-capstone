"""Program to count the number of votes for political parties
Joseph Preyer
24 April 2014"""

list1=[]

print("Independent Electoral Commission\n"+32*"-")
print("Enter the names of parties (terminated by DONE):\n")

# Get strings from user and add to dictionary
parties = {} # create empty dictionary "parties"
add=input("")
while add!="DONE":
    if add in parties:
        parties[add]+=1 #If the key is already in dictionary, add 1 to value
    else:
        parties[add]=1 #Otherwise add new key with value=1 to parties
    add=input("")

print("Vote counts:")

#create list of party names
names=[]
for i in parties:
    names.append(i)
names.sort()

#print out names and number of votes

for i in names:
    print (i, " "*(11-len(i)), "- ", parties[i],sep="")
    