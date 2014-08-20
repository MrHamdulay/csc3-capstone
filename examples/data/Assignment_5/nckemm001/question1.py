# Assignment 5: Question 1
# nckemm001
# 16 April 2014

def main():
# Print out the BBS MENU at the start of the programme
    bbs=("Welcome to UCT BBS\n"+"MENU\n"+"(E)nter a message\n"+"(V)iew message\n"+"(L)ist files\n"+"(D)isplay file\n"+"e(X)it")
    print(bbs)
    
    x = "y"
    while x == "y":
        choice = input("Enter your selection:\n")
        if choice == "X" or choice == "x":
            print("Goodbye!")
            break
        else:
            while choice != "X":
                if choice == "E" or choice == "e":
                    y = input("Enter the message:\n")
                    print(bbs)
                    
                    x = "y"
                    break
                elif choice == "V" or choice == "v":
                    if y=="":
                        print("The message is: no message yet")
                        print(bbs)
                        break
                    else:
                        print("The message is:",y)
                        print(bbs)
                        break
                    x = "y"
                elif choice == "L" or choice == "l":
                    print("List of files: 42.txt, 1015.txt")
                    print(bbs)
                    x = "y"
                    break
                elif choice == "D" or choice == "d":
                    u = input("Enter the filename:\n")
                    if u == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                        print(bbs)
                        x = "y"
                        break
                    elif u == "1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                        print(bbs)
                        x = "y"
                        break
                    else:
                        print("File not found")
                        print(bbs)
                        x = "y"
                        break
                elif choice == "X" or choice == "x":
                    x != "y"
    
main()
            
        