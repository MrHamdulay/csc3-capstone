stringlist = [] 
#prompt for string objects that will be added into list
inputstrings = input ("Enter strings (end with DONE): \n")

while inputstrings != "DONE":
    stringlist.append(inputstrings) #add each input into the string list
    inputstrings = input("") # ask for another input until "DONE"
print()
if len(stringlist)>0:
    maxlength = (max(len(s) for s in stringlist))
    alignment=">{}".format(maxlength)
    print("Right-aligned list:")
    for s in stringlist:
        print(format(s, alignment))
else:
    print("Right-aligned list: \n")
