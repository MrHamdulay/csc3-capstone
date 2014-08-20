"""program to print a list
Michelle Lu
27 April 2014"""

#create the list
string1=[]
word=input("Enter strings (end with DONE):\n")
print()
while word!="DONE":
    string1.append(word)
    word=input("")

print("Unique list:")

#create a new list
string2=[]
for i in string1:
    if i not in string2:
        string2.append(i)
        print(i)
