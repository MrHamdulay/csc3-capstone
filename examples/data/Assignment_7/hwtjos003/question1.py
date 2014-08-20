#unique list
#Joshua Hewitson
#2/5/2014

#create dictionary and list 
mydict = {}
mylist = []

# loop input while adding to 'mylist' - sentinel is 'DONE'
x = input("Enter strings (end with DONE):\n")
print('')
while x != "DONE":
    mylist.append(x)
    x = input("")
    
# get rid of multiple entries by making them dictionary keys
for i in mylist:
    mydict[i] = mylist.index(i)

# print out the list and order it based on the values in the dictionary 
print("Unique list:")
for i in range(len(mylist)):
    for j in mydict.keys():
        if mydict[j] == i:
            print(j)

