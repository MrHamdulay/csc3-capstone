#program to simulate BBS system
#By Chloe Longmore
#15 April 2014

#errors to fix: view option, file1 option
#print selection menu
def main_menu():
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    selection()



def selection():
    ans_1=input("Enter your selection:\n")
    file1='The Meaning of life is blah blah blah ...'
    file2='Computer Science class notes ... simplified'"\n"'Do all work'"\n"'Pass course'"\n"'Be happy'
    message1=''
    #selection enter message
    if ans_1=='E' or ans_1=='e': 
        message=input("Enter the message:\n")
        message1=message
        main_menu()
    # view message   
    if ans_1=='V' or ans_1=='v':
        if message1=='':
            print("no message yet")
        else:
            print("The message is:",message1)
        main_menu()
    # list files
    if ans_1=='L' or ans_1=='l':
        print("List of files: 42.txt, 1015.txt")
        main_menu()
    # display files
    if ans_1=='D' or ans_1=='d':
        file=input("Enter the filename:\n")       
        if file[0]=='1':
            print(file2)
        elif file[0]=="4":
            print(file1)         
        else:
            print("File not found")
        main_menu()
    #exit program   
    if ans_1=='x' or ans_1=='X':
        print("Goodbye!")
        
main_menu()   