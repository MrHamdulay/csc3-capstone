#program simulating a BBS
#gary Finkelstein
#15 April 2014

#Declaring a list of string variables to be used
a = 'Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it'
c = "The message is:"
d = "Goodbye!"
e = "List of files: 42.txt, 1015.txt"
f = "The meaning of life is blah blah blah ..."
g ="Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy"
h = "File not found"
i = "no message yet"
k = ""

#Start BBS: ask for user selection
print (a)
user_input =input ("Enter your selection: \n" )
x = user_input.upper()

#Determining whether the user has exited or continued with the program
if x == "X":
    print(d)
while x != "X":
    
    #user has continued with program, this code allows the user to enter a message
    while  x == "E":
        k = k+ input ("Enter the message: \n")
        print (a)
        user_input =input ("Enter your selection: \n" )
        x = user_input.upper()
        if x == "X":
            print(d) 
        break
    #this code allows the user to enter view the previously written message
    while x == "V":
            if k == "":
                print (c, i)
            else: 
                print(c, k)
            print (a)
            user_input =input ("Enter your selection: \n" )
            x = user_input.upper()
            if x ==  "X":
                print (d)
            break
        
       #this code allows the user to view a list of files
    while x == "L":
        print (e)
        print (a)
        user_input =input ("Enter your selection: \n" )
        x = user_input.upper()        
        if x == "X":
            print (d)
        break
    
    #this code allows the user to display a selected file from the list of files
    while x == "D":
        filename = input("Enter the filename: \n")
        if filename == "42.txt":
            print (f)
            print (a)
            user_input =input ("Enter your selection: \n" )
            x = user_input.upper()
            if x == "X":
                print (d)
            break
        elif filename == "1015.txt":
            print (g)
            print (a)
            user_input =input ("Enter your selection: \n" )
            x = user_input.upper()            
            if x== "X":
                print (d)
            break
        
        #this code allows is run if the file that a user enters does not exist
        else:
            print (h)
            print (a)
            user_input =input ("Enter your selection: \n" )
            x = user_input.upper()            
            if  x== "X":
                print (d) 
            break
        break
        
                
    