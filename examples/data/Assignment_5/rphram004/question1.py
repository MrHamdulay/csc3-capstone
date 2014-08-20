"""Question 1: programme that brings out options for the uses to choose from.
#Rama Raphalalani
#15-04-2014"""

print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
x = input("Enter your selection:\n")
y = x.lower()
a = '42.txt'
b = '1015.txt'

#the start point of the programme
#runs through all the options that the person can choose
while y!="eat":
        if y=='x':
                print("Goodbye!")
                break
        elif y=='e':
                z = input("Enter the message:\n")
                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                x = input("Enter your selection:\n")
                y = x.lower()
                if y=='v':
                        print("The message is:",z)
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        x = input("Enter your selection:\n")
                        y = x.lower()                
                        continue                        
                continue
        elif y=='v':
                if y=='v' and y!='e':
                        print("The message is: no message yet")
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        x = input("Enter your selection:\n")
                        y = x.lower()                
                        continue
        elif y=='l':
                print("List of files: ",a,","," ", b,sep='')
                print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                x = input("Enter your selection:\n")
                y = x.lower()
                if y=='v':
                        print("The message is:",z)
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        x = input("Enter your selection:\n")
                        y = x.lower()                
                        continue 
                continue  
        elif y=='d':
                c = input("Enter the filename:\n")

                if c==a:
                        print("The meaning of life is blah blah blah ...")
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        x = input("Enter your selection:\n")
                        y = x.lower()                        
                        continue
                elif c==b:
                        print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        x = input("Enter your selection:\n")
                        y = x.lower()                        
                        continue
                elif c!=a or c!=b:
                        print("File not found")
                        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
                        x = input("Enter your selection:\n")
                        y = x.lower()                        
                        continue                

                
                        
        
        
    