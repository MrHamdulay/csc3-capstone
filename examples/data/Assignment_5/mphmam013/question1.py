"""assignment 5
question1
13 april 2014
Mphuthi Mamorena"""

def main():
    list=["42.txt","1015.txt"]
    a=''
    v=''
    while a!='X' or a!='x':
        print("Welcome to UCT BBS")
        print("MENU")
        print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")        
        a=input("Enter your selection:\n")
        if a=='x' or a=='X':break
        if a=='E'or a=='e':
            v+=input("Enter the message:\n")
        elif a=='V' or a=='v':
            if v!='':
                print("The message is:",v)
            else:
                print("The message is: no message yet")
        elif a=='l'or a=='L':
            print("List of files:","42.txt,","1015.txt")
        elif a=='d'or a=='D':
            f=input("Enter the filename:\n")
            if f not in list:
                print("File not found")
            elif f==list[0]:
                print("The meaning of life is blah blah blah ...")
            elif f==list[1]:
                print("Computer Science class notes ... simplified")
                print("Do all work")
                print("Pass course")
                print("Be happy")

    print("Goodbye!")
main()

                

                
                
                
        