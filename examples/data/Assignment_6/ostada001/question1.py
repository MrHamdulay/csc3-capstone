#Right alignment program
#Adam Oosthuizen

'''Aligns a list of user input words so that the last letter of each forms a straight line'''
names = []
entries=""


def getLongestEntry(x=["x","y"]):
    ''' determines the longest string in an array'''
    largest=0
    for i in range (0,len(x)):
        if len(x[i]) > largest:
            largest = len(x[i])
            
    return largest

print("Enter strings (end with DONE):")

while entries != "DONE":
    entries = input()
    if entries !="DONE":
        names.append(entries)
        entries =""
print()
print("Right-aligned list:")
longest = getLongestEntry(names)
for i in range (0,len(names)):
    print((longest-len(names[i]))*" ",names[i],sep="")
    
        
    