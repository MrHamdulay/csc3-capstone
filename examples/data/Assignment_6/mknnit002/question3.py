#mknnit002
#question 3 ass 6

print("Independent Electoral Commission")
print("--------------------------------")


print("Enter the names of parties (terminated by DONE):\n")

votelist=[]
while (True):
    vote=input()
    if vote=="DONE":
        break
    else:
        votelist.append(vote)

print("Vote counts:")
votelist.sort()
while votelist!=[]:
    i=votelist[0]
    count=votelist.count(i)
    print(i.ljust(10),"-",str(count))    
    for k in range(count):
        votelist.remove(i)
        

    