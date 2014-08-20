"""printing a list of strings without duplicates
Jacqueline Blomendahl
29/04/2014"""
#getting input and creating empty lists
string=input("Enter strings (end with DONE):\n")
List=[]
List.append(string)
unique_list=[]
#while loop creating first list of srtings
while string!= "DONE":
    string=input()
    List.append(string)
del List[-1]
#creating a list with unique strings
for i in (List):
    if not (i in unique_list):
        unique_list.append(i)
#printing the lists
print()
print("Unique list:")
for i in unique_list:
    print(i)

