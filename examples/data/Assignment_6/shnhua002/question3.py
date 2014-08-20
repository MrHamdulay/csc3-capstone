#Charlie Shang
#SHNHUA002
#Assignment 6 Q3

arr=['']
print("Independent Electoral Commission\n" + '-' * 32 + "\nEnter the names of parties (terminated by DONE):\n")

while arr[-1]!="DONE": #while the last item in the list is not "DONE"
     arr.append(input())

arr.sort() #arranges list alphabetically
arr.remove("DONE") 
arr.append(" ") #add an extra element for comparison purposes later

print("Vote counts:")
for i in range(1,len(arr)-1,1):
     if arr[i]!=arr[i+1]: #if the next item is not a duplicate, since sorted alphabetically
          print(arr[i].ljust(11)+"-",arr.count(arr[i]))
         