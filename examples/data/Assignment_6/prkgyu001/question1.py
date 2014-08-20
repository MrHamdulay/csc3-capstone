#get the list of names and save it as an object!
def getNames():
    lists = []
    x=input("Enter strings (end with DONE): \n")
    while x != "DONE":
        lists.append(x)
        x = input("")
    return lists

# we have to align the list to the right so we must find the element with maximum characters.   
def themaxfinder(lists):
    newlist = []
    indices = 0
    for i in lists:
        x = len(lists[indices])
        newlist.append(x)
        indices = indices + 1
    newlist.sort()
    newlist.reverse()
    return newlist[0]



y = getNames()
z = themaxfinder(y)
print()


#using the maximum number, we create spacing and then print 
def aligner(lists,maxvalue):
    print("Right-aligned list: ")
    for i in lists:
        spacing = maxvalue - len(i)
        print((" "*spacing)+i)
        
aligner(y,z)