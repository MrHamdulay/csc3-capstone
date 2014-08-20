#ComSci Assignment 6
#Nikhil Jiten Naik
#25/04/2014
#Question 3

votes={}
group=input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while group!="DONE":
  
    if group in votes.keys():
        votes[group]+=1
    else:
        votes[group]=1
    group=input('')
print()
print("Vote counts:")
for key in sorted(list(votes.keys())):
    print(key.ljust(10),"-",votes[key])