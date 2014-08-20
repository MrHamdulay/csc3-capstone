"""program to count number of votes for each political party
vuyolwethu nkosi
23 april 2014"""

#create empty list
name=[]
#get list of votes from user
print("Independent Electoral Commission","-"*32,sep="\n") 
names=input("Enter the names of parties (terminated by DONE):\n")
#print list
while names!="DONE":
    name.append (names)
    names=input("")
    #name.sort
print("\nVote counts:")
#create dictionary to store the count of votes
count={}
for i in name:
    if i not in count: #if the name is not found in the dictionary, add it in dictionary
        count[i]=1 #key is equals to 1
    else: #if its found in the counter, add 1 to it
        count[i]+=1

#add to list
for i in sorted(count.keys()):
    print(i.ljust(10),"-",(count[i])) #print the word, then "-", then print the vote count

