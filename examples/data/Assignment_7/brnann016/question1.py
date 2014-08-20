#enter list of strings that is re-printed without duplicates(same order)
#annika brundyn
#30/04/14

#get input from user and create list
print("Enter strings (end with DONE):")
list1=[]
string=input("")
while string!="DONE":
    list1.append(string)
    string=input("")
    
#create a new list(ulist) of values from list1 that are not in ulist yet
ulist = []
for string in list1:
   if string not in ulist:
       ulist.append(string)

#print new unique list
print()
print("Unique list:")
for i in ulist:
    print(i)


