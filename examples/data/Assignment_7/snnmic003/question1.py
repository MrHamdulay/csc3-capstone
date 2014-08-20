# Question 1 Assignment 7, Remove Duplicate
# Michael Sanne
# 2014/05/01

#Allows user to enter a list
list = []
option = input ("Enter strings (end with DONE):\n")

while (option != "DONE"):
    list.append (option)
    option = input()
#Creates a list without duplicate elements called noDuplicate    
noDuplicate = []
for i in range (len(list)):
    if (not list[i] in noDuplicate):
        noDuplicate.append (list[i])
#Prints out the noDuplicate list
print()
print ("Unique list:")
for i in range (len(noDuplicate)):
    print (noDuplicate[i])