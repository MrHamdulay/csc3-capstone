# Program to simulate a BBS
# Wandile Lesejane
# 14 April 2014
 
# files
def list_files():
    print("List of files: 42.txt, 1015.txt")
    

def disp_file1():
    txt1="The meaning of life is blah blah blah ..."
    print(txt1)
def disp_file2():
    txt2="Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"
    print(txt2)

# combine all functions

E="no message yet"
SC=""
while SC!='X' or SC!='x':
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    SC=input("Enter your selection:\n")
    if SC=='E' or SC=='e':
        E=input("Enter the message:\n")
        
    elif SC=='V' or SC=='v':
        print("The message is:",E)
    elif SC=='l' or SC=='L':
        list_files()
    elif SC=='d' or SC=='D':
        SC2=input("Enter the filename:\n")
        if SC2=='42.txt':
            disp_file1()
        elif SC2=='1015.txt':
            disp_file2()
        else:
            print("File not found")
    elif SC=='X' or SC=='x':
        print("Goodbye!")
        break

        
            