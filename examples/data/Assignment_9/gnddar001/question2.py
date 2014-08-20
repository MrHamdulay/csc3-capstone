#Darryl Gounden
#12/05/14
#Text formatter


putin = input("Enter the input filename:\n")
putout = input("Enter the output filename:\n")
limit = eval(input("Enter the line width:\n"))

#Opens the file that you want to and reads all of the lines into a list.
f = open(putin,"r")

listed = f.readlines()

f.close()


#Deletes all of the "\n" characters in the list.
for i in range(len(listed)):
    if listed[i][-1] == "\n":
        listed[i] = listed[i][:-1]
        
#Seperates each item in the list by a " ". Creating a list of lists.
for i in range(len(listed)):
    listed[i] = listed[i].split(" ")

#If a list in the list is an empty string, make it a !. Used later as a marker to find the correct place to leave a line.
for i in range(len(listed)):
    if listed[i] == [""]:
        listed[i] = ["!"]

list_1 = []
list_2 = []

#Merge the list of lists into one list.
for i in range(len(listed)):
    for j in range(len(listed[i])):
        list_1.append(listed[i][j])

def printer(listing):
    global list_1
    global list_2
    count = 0
    
    #If this is the last line left to print.
    if len(" ".join(listing)) <= limit:
        for i in range(len(listing)):
                    #If the marker for leaving a line is found, do so.
                    if listing[i] == "!":
                        print(" ".join(list_2), file=g)
                        print("",file=g)
                        list_2 = []
                        return printer(listing[i+1:])
                    #Or continue appending to temporary list.
                    else:
                        list_2.append(listing[i])
        #If no if statement is reached, print the entire last line.            
        else:
            print(" ".join(listing), file=g)
        
    else:
        for i in range(len(listing)):
            count += len(listing[i])
            #Checks for the marker to leave a line.
            if listing[i] == "!":
                print(" ".join(list_2), file=g)
                print("",file=g)
                list_2 = []
                return printer(listing[i+1:])
            #Adds to the temporary list.
            elif count <= limit:
                list_2.append(listing[i])
            #If "limit" is exceeded, empty temporary list and print it.    
            elif count > limit:
                print(" ".join(list_2), file=g)
                list_2 = []
                return printer(listing[i:])
            #This is to account for spaces in between words.
            count += 1

#Opens the file you want to write to, or creates a file.                  
g = open(putout,"w")  

printer(list_1)

g.close()


           
    
            
        
            
            
        
        
    
                   
        
    