'''program for list with sentinel
nicole henning
due: 25 april'''

#make a list
names_tot = []

#get list
names_str = input("Enter strings (end with DONE):\n")

if names_str == "DONE": #for no list
    print()
    print("Right-aligned list:")
    
else:
    while names_str != "DONE": #while not done, open space for next name
        names_tot.append(names_str) #add each name to existing list
        names_str = input("")
        
    length = len(max(names_tot, key = len)) #for lenth of alignment
    length = int(length)
    
    print()
    print("Right-aligned list:")
    
    #then print list right alligned
    for names_str in names_tot:
        print(names_str.rjust(length)) #right justified with length spaces
        