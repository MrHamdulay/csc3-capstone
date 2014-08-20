#question3
#Author: Dipanjali Samoo
#Student Number: SMXDIP001


print("Independent Electoral Commission")
print("--------------------------------")
n= input("Enter the names of parties (terminated by DONE):\n")
array=[]
array.append(n)
while n!="DONE":
    n= input("")
    array.append(n)
array_len= len(array)
array= array[0:array_len-1]
array.sort()

while n=="DONE":
    break

#this loop is used to populate dictionary with parties from list 
v={}
for i in array:
    if not i in v:
        v[i]=1
    else:
            v[i] =v[i]+1
        
#printed output
print('\n' "Vote counts:")
for i in array:
    while array.count(i)>1:
        array.remove(i)
for i in array:
    a= "{0:<10}".format(i)
    print(a," - ",v[i],sep="")