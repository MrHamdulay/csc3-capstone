"""Assignment 6 question 1
shannon clacey
23 april 2014"""
def name():
    names = [] #create an emtpy string in which to add everything
    name = input("Enter strings (end with DONE): \n")
    while name != "DONE": #create loop where user is asked for input until they enter DONE
        names.append(name) #keep adding the given name to the names list
        name = input() #continue to get input to add to list
    print()
    max = 0 #create variable to terminate the loop when it equals this
    for i in names: #this loop determines the length of the longest word in the names list
        if len(i)>=max:
            max=len(i)
    print("Right-aligned list:")
    for j in names: #print the list with it being right justified in accordance to the longest word
        print((max-len(j))*" ", j, sep='')
name()    
    