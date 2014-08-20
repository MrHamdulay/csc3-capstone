"""The program finds the unique strings in a list
Rivoningo Seweya
27 April 2014"""

#create an empty list
strings=[]
string=input("Enter strings (end with DONE):\n")
#create a sentinal loop and append strings to the list
while string!= "DONE":
    if string not in  strings:
        strings.append(string)
    string=input("")
print("")
#print the keys of the ditionary
print("Unique list:")
#uni_list=[]
for i in strings:
    print(i)