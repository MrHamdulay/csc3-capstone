"""A program to simulate a BBS
Simlindile Mahlaba
17 April 2014"""

menu="Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
no_msg="no message yet"
files= "42.txt, 1015.txt"
file1="The meaning of life is blah blah blah ... "
file2="Computer Science class notes ... simplified \nDo all work \nPass course \nBe happy"
selections= "E" , "V" , "L" , "D" ,"X" , "e", "l", "v" , "d" , "x"

print(menu)
sen=input("Enter your selection: \n")
x=sen.upper()
y=""
while x!="X":
            if x == "E":
                        y = input("Enter the message: \n")
            elif x == "V"and y == "":
                        print("The message is: no message yet")
            elif x == "V" and  y !="":
                        print("The message is:", y)
            
            elif x == "L": 
                        print("List of files:", files)
            elif x == "D":
                        t=input("Enter the filename:\n")
                        if t == "42.txt":
                                    print(file1)
                        elif t == "1015.txt":
                                    print(file2)
                        else:
                                    print("File not found")
            print(menu)
            sen=input("Enter your selection: \n")
            x=sen.upper()            
print("Goodbye!")
      