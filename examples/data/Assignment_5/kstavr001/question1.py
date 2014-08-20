#Assignment 5, Question 1
#Avreyna Kistensamy
#13 April 2014

#Using often,function convenient
def menu(): 
    options = "Welcome to UCT BBS\n"
    options += "MENU\n"
    options += "(E)nter a message\n"
    options += "(V)iew message\n"
    options += "(L)ist files\n"
    options += "(D)isplay file\n"
    options += "e(X)it"  
    print(options)

def main():
    y = ""
    menu()
    #initializing loop
    i_l = "s"
    while i_l == "s": 
        choice = input("Enter your selection:\n")
        choice = choice.lower()
        if choice == "x":
            print("Goodbye!")
            break #exiting loop as user requested
        else:
            while choice != "x":
                if choice == "e":
                    y = input("Enter the message:\n")
                    menu()
                    i_l = "s"
                    break
                elif choice == "v":
                    if y=="":
                        print("The message is: no message yet")
                        menu()
                        break
                    else:
                        print("The message is:",y)
                        menu()
                        break
                    i_l = "s"
                elif choice == "l":
                    print("List of files: 42.txt, 1015.txt")
                    menu()
                    i_l = "s"
                    break
                elif choice == "d":
                    u = input("Enter the filename:\n")
                    if u == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                        menu()
                        i_l = "s"
                        break
                    elif u == "1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                        menu()
                        i_l = "s"
                        break
                    else:
                        print("File not found")
                        menu()
                        i_l = "s"
                        break
                elif choice == "x":
                    i_l != "s" 
    
main()
            
        