print("Independent Electoral Commission")
print("--------------------------------")
names= input("Enter the names of parties (terminated by DONE):\n")#prompt user for input of parties

array=[]
array.append(names)
while names!="DONE":
    names= input("")
    array.append(names)
array_len= len(array)
array= array[0:array_len-1]
array.sort()
   
while names=="DONE":
    break

votes={}
for i in array:
    if not i in votes:
        votes[i]=1
    else:
        votes[i] = votes[i]+1
  
print('\n'"Vote counts:")
for i in array:
    while array.count(i)>1:
        array.remove(i) #remove duplicate values from list
for i in array:
    x= "{0:<10}".format(i)
    print(x," - ",votes[i],sep="")
