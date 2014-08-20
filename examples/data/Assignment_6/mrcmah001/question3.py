print("Independent Electoral Commission")
print("--------------------------------")

x=""
list1=[]
list2=[] #empty lists
print("Enter the names of parties (terminated by DONE):")
while x != "DONE": #specify when adding ends
    x=input()
    if x!= "DONE":
        list1.append(x)
for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i) #when does i add and when does it not
list2.sort() #sort list
print('\nVote counts:')
for item in list2:
    print(item+(' '*(10-len(item)+1))+'- '+str(list1.count(item))) #number of spaces after words

        