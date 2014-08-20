"""Assignment 6, question 1:Prints out a list of right alligned names
Dean Gracey
19 April 2014"""

list_names = []
newname= input("Enter strings (end with DONE):\n")


#populates a list with names, ending with DONE
while (newname!="DONE"):
    list_names.append(newname)
    newname = input("")

longest = 0     
for name in list_names:
    if (len(name)>longest):
        longest = len(name)
longest = str(longest) 

print("\nRight-aligned list:")
for name in list_names:
    toformat = "{0:>"+longest+"}"
    print(toformat.format(name))
    