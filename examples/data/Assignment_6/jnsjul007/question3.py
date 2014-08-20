#program to count the number of votes for inputted parties
#Julian van Rensburg
#program to count party votes
#Julian van Rensburg
#24 April 2014

#print opening statement
print("Independent Electoral Commission\n","--------------------------------", sep='')
#create empty list
x=[]
#get votes
y=input("Enter the names of parties (terminated by DONE):\n")
while not y=="DONE":
    x.append(y)
    y=input('')

#create new list, add names to list as they appear in x
z=[]
for i in x:
    if i not in z:
        z.append(i)
#sort function        
z.sort()
print("\nVote counts:")
for i in z:
    a=x.count(i)
    f="{0:<10}".format(i)
    print(f,"-",a)