strings = input("Enter strings (end with DONE):\n")
listofStrings=[]
while (strings !="DONE"):
   if strings not in listofStrings:
      listofStrings.append(strings)
   strings=input()
print("\nUnique list:")
for i in listofStrings:
   print(i)