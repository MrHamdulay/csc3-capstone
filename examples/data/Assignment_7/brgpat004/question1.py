'''Q1 of Assignment 7: Removing Duplicates
Patrick Boroughs
27 April 2014'''

print("Enter strings (end with DONE):")
string=input()
listS=[]

while (string !='DONE'):        #sentinal DONE
    if string not in listS:
        listS.append(string)    #add to list
    string=input()              #receive more input

#print new list
print("\nUnique list:")    
for string in listS:
    print(string)