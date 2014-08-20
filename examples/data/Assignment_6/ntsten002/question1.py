#question1
#Tendani Netshitenzhe
#25 April 2014

#Create an empty list
mylist = []

#Get list of strings
names = input("Enter strings (end with DONE):\n")
while names != "DONE":
    mylist.append(names)
    names = input("")

#Get the length of the list    
length = len(mylist)

print("\nRight-aligned list:")

width = 0
for i in range(length):
    if len(mylist[i]) > width: #Get length of the string with the max length
            width = len(mylist[i]) #Assign it to width
            
for i in range(length):
    name = mylist[i]
    print(name.rjust(width)) #printing aligned list
    

