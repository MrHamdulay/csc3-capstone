"""Zikho Godana
15 April 2014
a program to simulate a simple Bulletin Board System(BBS) with one stored message and 2 fixed files"""

def name():
        print("Welcome to UCT BBS\nMENU")
        
def menu():
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
def main():
        while True:
                name()
                menu()
                selection=input("Enter your selection:\n")
                if selection=='v':
                        print("The message is: no message yet")
                elif selection in 'Ee':
                        message=input("Enter the message:\n")
                elif selection== 'V':
                        
                        if message=="":
                                message="no message yet"
                        else:
                                
                                print("The message is:",message)
                
                elif selection=='l':
                        print("List of files: 42.txt, 1015.txt")
                elif selection=='d':
                        filename=input("Enter the filename:\n")
                        if filename=='42.txt':
                                file1=open("42.txt","w+")
                                file1.write("The meaning of life is blah blah blah ...")
                                file1.close()
                                file1=open('42.txt','r')
                                print(file1.read())
                        elif filename=='1015.txt':
                                file2=open("1015.txt","w+")
                                file2.write("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                                file2.close()
                                file2=open("1015.txt","r")
                                print(file2.read())
                        else:
                                print("File not found")
                elif selection=='x' or 'X':
                        print("Goodbye!")
                        break
                
main()      
    