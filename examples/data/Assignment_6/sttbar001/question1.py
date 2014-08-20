""" list of strings
barak setton 
19/04/2014"""
length = 0 
longname =""
counter =0
namelist = []
name = input("Enter strings (end with DONE): \n")

while name != "DONE":
    length = len(name)
    if len(longname) < length: # finding the longest name 
        longname = name
    namelist.append(name)   # adding name to lists
    counter = counter + 1               # increasing integer
    name = input()
print("")
print("Right-aligned list:")
for i in range(len(namelist)):
    print("{name:" ">{width}}".format(name = namelist[i], width = len(longname)))  # formating the print
    