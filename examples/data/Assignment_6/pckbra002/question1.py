"""List of strings are entered by the user, ended by the sentinal 'DONE', and then the list is printed out right alligned with the longest string"""
#Bandon Pickup (PCKBRA002)
#2014/04/21
#Assignment 6 Question 1
name = input("Enter strings (end with DONE):\n")
names=[]
length=0
while name!= "DONE":
    names.append(name)
    if len(name)>length:#checks to see if the length of the next word is longer than our current longest length
        length=len(name)
    name = input("")#continues getting input without telling the user again what to do
print()
print("Right-aligned list:")
for name in names:#for every name in the names array, the name is printed
    print(" "*(length-len(name)),name,sep="")#number of spaces is the length of the longest string minus the length of this string
    