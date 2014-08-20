#Shaaheen Sacoor SCRSHA001
#16 April 2014
#Program to to display Bulleitin Board that can
#Enter,View,List and Display messages and files

def main():
    # Assigning menu to variable bbs
    bbs = "Welcome to UCT BBS\n"
    bbs += "MENU\n"
    bbs += "(E)nter a message\n"
    bbs += "(V)iew message\n"
    bbs += "(L)ist files\n"
    bbs += "(D)isplay file\n"
    bbs += "e(X)it"
    y = ""
    print(bbs)
    t = "p" #for the while loop as t will equal p and keep while loop
    while t == "p":  # running. t and p are random variables
        sel = input("Enter your selection:\n") 
        if sel == "X" or sel == "x": #if need to exit straight away
            print("Goodbye!")
            break
        else:
            while sel != "X": #inner while loop that repeats menu
                if sel == "E" or sel == "e":
                    y = input("Enter the message:\n")
                    print(bbs)
                    t = "p" # will make the menu loop again
                    break
                elif sel == "V" or sel == "v":
                    if y=="": #if input is empty print this
                        print("The message is: no message yet")
                        print(bbs)
                        break
                    else:
                        print("The message is:",y)
                        print(bbs)
                        break
                    t = "p"
                elif sel == "L" or sel == "l":
                    print("List of files: 42.txt, 1015.txt")
                    print(bbs)
                    t = "p"
                    break
                elif sel== "D" or sel == "d":
                    u = input("Enter the filename:\n")
                    if u == "42.txt":
                        print("The meaning of life is blah blah blah ...")
                        print(bbs)
                        t = "p"
                        break
                    elif u == "1015.txt":
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                        print(bbs)
                        t = "p"
                        break
                    else:
                        print("File not found")
                        print(bbs)
                        t = "p"
                        break
                
    
main()
            
        