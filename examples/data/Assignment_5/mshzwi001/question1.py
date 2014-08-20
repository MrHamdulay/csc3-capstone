# a program which is presented with a set of options, one of which is selected to perform a particular task
# mashau zwivhuya
# 13/ 04 /2014
def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")    
       
def main():
    menu()
    selection=3
    message="no message yet"
    while selection !=-1:
        selection=input("Enter your selection:\n")
        if selection=="E" or selection=="e":
            message=input("Enter the message:\n")
        if selection=="V"or selection=="v":
            print("The message is:",message)
        if selection=="L"or selection=="l":
            print("List of files:","42.txt, 1015.txt")
        if selection=="D" or selection =="d":
            jin=input("Enter the filename:\n")
            if jin=="42.txt":
                print("The meaning of life is blah blah blah ...")
            elif jin=="1015.txt":
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")
            else :
                print("File not found")
        if selection =="X" or selection=="x":
            print("Goodbye!")
            break
        menu()
        
main()        