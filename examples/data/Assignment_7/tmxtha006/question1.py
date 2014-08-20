"""This program prints out a list of strings in the same order without duplicates
Hebert Tema
28-04-2014"""



#create an empty list for storing the input
list_strings=[]

#get the input from the user
string=input("Enter strings (end with DONE):\n")

#while the user doesnt exit append the input and get anotherinput
while string!="DONE":
    if string not in list_strings:
        list_strings.append(string)
    string=input()
    
#return a list of string in the same order
print("\nUnique list:")
for i in list_strings:
    print(i)