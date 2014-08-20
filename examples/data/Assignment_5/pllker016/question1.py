#Start up menu
#kereshnee pillay
# 14 april 2014

# list all selections
def main():
    x = "Welcome to UCT BBS\n"
    x += "MENU\n"
    x += "(E)nter a message\n"
    x += "(V)iew message\n"
    x += "(L)ist files\n"
    x += "(D)isplay file\n"
    x += "e(X)it"
    y = ""
    print(x)
    
    #let user input their choice and check input
    t = "p"
    while t == "p":
        choice = input("Enter your selection:\n")
        if choice == "X" or choice == "x":
            print("Goodbye!")
            break
        else:
            while choice != "X":
                if choice == "E" or choice == "e":
                    y = input("Enter the message:\n")
                    print(x)
                    
                    t = "p"
                    break
                elif choice == "V" or choice == "v":
                    if y=="":
                        print("The message is: no message yet")
                        print(x)
                        break
                    else:
                        print("The message is:",y)
                        print(x)
                        break
                    t = "p"
                elif choice == "L" or choice == "l":
                    print("List of files: 42.txt, 1015.txt")
                    print(x)
                    t = "p"
                    break
                elif choice== "D" or choice == "d":
                    u = input("Enter the filename:\n")
                    if u == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                        print(x)
                        t = "p"
                        break
                    elif u == "1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                        print(x)
                        t = "p"
                        break
                    else:
                        print("File not found")
                        print(x)
                        t = "p"
                        break
                elif choice == "X" or choice == "x":
                    t != "p"
    
main()
            
        