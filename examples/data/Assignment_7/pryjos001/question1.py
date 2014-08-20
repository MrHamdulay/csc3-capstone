"""Program to delete duplicates from a list of strings
Joseph Preyer
29 April 2014"""

#Get list1 of strings from user

list1=[]

# Get strings from user and add to list
print("Enter strings (end with DONE):")
add=input("")
while add!="DONE":
    list1.append(add)
    add=input("")

#Create new empty list2
list2=[]

print ("\nUnique list:")

#If string from list1 not in list2, print it
for i in list1:
    if i not in list2:
        print (i)
        list2.append(i) #Each time a string is printed, add it to list2

