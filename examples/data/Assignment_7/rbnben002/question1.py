list1=[]
counter=0
user=input("Enter strings (end with DONE):\n")
while (user !="DONE"):
   if user not in list1:
      list1.append(user)
   user=input()
print("\nUnique list:")
for i in list1:
   print(i)