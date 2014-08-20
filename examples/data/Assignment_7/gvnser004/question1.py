"""
Serayen Govender
GVNSER004 
question1 
print unique list form list

"""
arr=[]
#list of strings
arr_unique=[]
#list of unique strings
inp=input("Enter strings (end with DONE):\n")

while inp!="DONE":
      arr.append(inp)
      inp=input()
      #input list of strings

for i in range(len(arr)):
      if(arr.index(arr[i])==i):
            arr_unique.append(arr[i])   
            #add unique elements to unique list

print()
print("Unique list:")
for i in arr_unique:
      print(i)
#print list of unique strings