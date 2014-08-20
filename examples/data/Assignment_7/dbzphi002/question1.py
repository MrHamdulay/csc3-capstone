#Thembekile Dubazana
#dbzphi002
#Assignment7:Q1

"""Create a list without duplicates and in original order"""

#The input
strings=[]
newstr=[]
words=input("Enter strings (end with DONE):\n")

#Loop for entering words
while words!="DONE":
    strings.append(words)
    words=input()
    
#Loop for checking the duplicates   
for i in range(len(strings)):
    check=strings[i] in newstr
    if check==False:
        newstr.append(strings[i])

#Printed list
print()
print("Unique list:")
for j in newstr:
    print(j)