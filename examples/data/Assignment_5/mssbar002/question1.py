"""Program to simulate BBS board
Author: Barnett Msiska
Date: 14/04/2014"""

def main():
    header()
    selection = select()
    selection = selection.lower()
    message = ""
    file1Name = "42.txt"
    file1Content = "The meaning of life is blah blah blah ..."
    file2Name = "1015.txt"
    file2Content = "Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"

    while (selection != 'x'):
        if selection == 'e':
            message = input("Enter the message:\n")  
        elif selection == 'v':
            if message == "":
                print("The message is: no message yet")
            else:
                print("The message is:" , message)      
        elif selection ==  'l':
            print("List of files:", file1Name + ",", file2Name) 
        elif selection == 'd':
            fileName = input("Enter the filename:\n")
            if fileName == file1Name:
                print(file1Content)
            elif fileName == file2Name:
                print(file2Content)
            else:
                print("File not found")

        header()
        selection = select()  
        selection = selection.lower()
    
    print("Goodbye!")    

def header():
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")   
    
def select():
    select = input("Enter your selection:\n") 
    return select
    
    
main()