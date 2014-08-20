"""Shriya Roy
16 April 2014
BBS"""



def main():
    #initial assignment
    a = 'no message yet'
    l= ["42.txt" , "1015.txt"]
    while True:
        #printing menu
            print("Welcome to UCT BBS")
            print("MENU")
            print("(E)nter a message")
            print("(V)iew message")
            print("(L)ist files")
            print("(D)isplay file")
            print("e(X)it")
            
            x=input("Enter your selection:\n")
        
            
            if x== "E" or x == 'e' :
                a= input("Enter the message:\n")
            if x== "V" or x == 'v':
                a = print("The message is:", a)
            if x== "X" or x == 'x':
                print("Goodbye!")
                break
            if x == "l" or x == 'L':
                print ("List of files:" ,', '.join(l))
            if x== "d" or x == 'D':
                y= input("Enter the filename:\n")
                if y == "1015.txt":
                    print("Computer Science class notes ... simplified")
                    print("Do all work")
                    print("Pass course")
                    print("Be happy")
                
                if y == "42.txt":
                    print ("The meaning of life is blah blah blah ...")
            
            
                if y!= "1015.txt" and y!="42.txt":
                    print("File not found")

            
        
        
main()
