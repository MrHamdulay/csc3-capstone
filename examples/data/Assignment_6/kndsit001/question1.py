"""Program to right align names in a list
Sithasibanzi Kondleka
23 April 2014"""

names = []
name = input("Enter strings (end with DONE):\n") #get a list of names
while name != "DONE":
    names.append(name) #keep adding to the list
    name = input("")
print()
print("Right-aligned list:")
if len(names) != 0:
    gap = max(len(name) for name in names) #get the longest name
    
    for name in names:
        print(name.rjust(gap)) #right-align according to the longest name    
    