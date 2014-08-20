#Assignment 5
#13 April 2014
#Shannon Clacey

#I have assigneed random variables to each of the statements used in the program so that it is easy to call them later on
a = 'Welcome to UCT BBS \nMENU \n(E)nter a message \n(V)iew message \n(L)ist files \n(D)isplay file \ne(X)it'
c = "The message is:"
d = "Goodbye!"
e = "List of files: 42.txt, 1015.txt"
f = "The meaning of life is blah blah blah ..."
g ="Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy"
h = "File not found"
i = "no message yet"
k = ""

#initial printing of the menu
print (a)
x =input ("Enter your selection: \n" )
#option of first choice being to exit
if x == "x" or x == "X":
    print(d)

#Creating a while loop for when the first option is not to exit
while x != "x" and x != "X": #looking at both capital and small options but ensuring to use x= both times otherwise it would always be true
    #looking what happens when the first option is to deal with entering a message
    while x == "e" or x == "E":
        k += input ("Enter the message: \n")
        print (a)
        x =input ("Enter your selection: \n" )
        if x == "x" or x == "X":
            print(d) 
        break #breaking out of this loop to stop it being indefinite
    while x == "v" or x == "V": #creating another loop but now to deal with the possibility of viewing a message which might or might have been entered before
            if k == "":
                print (c, i)
            else: 
                print(c, k)
            print (a)
            x =input ("Enter your selection: \n" )
            if x == "x" or x == "X":
                print (d)
            break
    while x == "l" or x == "L": #creating while loop to run through the option of viewing the list of available files
        print (e)
        print (a)
        x =input ("Enter your selection: \n" )
        if x == "X" or x == "x":
            print (d)
        break
    while x == "D" or x == "d": #asking using to input the given files name and checking whether it is on the database or not. If it is, the file is returned and if not then the user is told that the file is not found
        m = input("Enter the filename: \n")
        if m == "42.txt":
            print (f)
            print (a)
            x =input ("Enter your selection: \n" )
            if x == "x" or x== "X":
                print (d)
            break
        elif m == "1015.txt":
            print (g)
            print (a)
            x =input ("Enter your selection: \n" )
            if x == "x" or x== "X":
                print (d)
            break
        else:
            print (h)
            print (a)
            x =input ("Enter your selection: \n" )
            if x == "x" or x== "X":
                print (d) 
            break
        #finally breaking out of the entire loop where the first option is not to exit
        break
        
                
    