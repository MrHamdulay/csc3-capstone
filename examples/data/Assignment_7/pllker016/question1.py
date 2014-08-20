#kereshnee pillay
#1 may 2014
#list without duplicates

#create a list
list=[]

#input into the list
string=input("Enter strings (end with DONE):\n")
while string.lower()!= "done":
    if not string in list:
        list.append(string)
    string=input()

#print output
print("\nUnique list:")
for i in list:
    print(i)