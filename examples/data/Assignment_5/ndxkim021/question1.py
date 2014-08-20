def main():
    bbs = "Welcome to UCT BBS\n"
    bbs += "MENU\n"
    bbs += "(E)nter a message\n"
    bbs += "(V)iew message\n"
    bbs += "(L)ist files\n"
    bbs += "(D)isplay file\n"
    bbs += "e(X)it"
    y = ""
    print(bbs)
    #sel = input("Enter your selection:\n")
    t = "p"
    while t == "p":
        sel = input("Enter your selection:\n")
        if sel == "X" or sel == "x":
            print("Goodbye!")
            break
        else:
            while sel != "X":
                if sel == "E" or sel == "e":
                    y = input("Enter the message:\n")
                    print(bbs)
                    #n = input("Enter your selection:\n")
                    t = "p"
                    break
                elif sel == "V" or sel == "v":
                    if y=="":
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
                elif sel == "X" or sel == "x":
                    t != "p"
    
main()
            
        