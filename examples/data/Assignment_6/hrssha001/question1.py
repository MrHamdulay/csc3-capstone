# Program to collect names and print them right aligned
#Shane Horsley
#20 April 2014
NAME_LIST=[]
name= input("Enter strings (end with DONE):\n") #get first name
print()
while name != "DONE":    # keep getting names until DONE is typed
    NAME_LIST.append(name) # add names to list
    name = input()
    
length = 0
for i in NAME_LIST: # check for longest name
    if len(i) > length:
        length = len(i)
print("Right-aligned list:")
for x in NAME_LIST:
    print((length-len(x))*" "+x) # could also have used formatting
                                 # had problem with getting the length in to "{:>length}"
        

    