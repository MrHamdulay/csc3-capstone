#use of if,while and for statements, author Gillian Wachira, date 15/04/2014


def main():
    k= "no message yet"
    y=("Welcome to UCT BBS\n""MENU\n""(E)nter a message\n""(V)iew message\n""(L)ist files\n""(D)isplay file\n""e(X)it")
    x=""
    while x!=("X") and x!=("x"):
        print(y)
        x=input("Enter your selection:\n")
        if x==("E") or x== ("e"):
                q=input("Enter the message:\n")
                
        elif x==("V") or x==("v"):
                print("The message is: "+k)
                        
                
        elif x==("l") or x==("L"):
                print("List of files: 42.txt, 1015.txt")
                        
                        
        elif x==("d") or x==("D"):
                h=input("Enter the filename:\n")
                if h==("42.txt"):
                        print("The meaning of life is blah blah blah ...")
                                
                elif h==("1015.txt"):
                        print("Computer Science class notes ... simplified")
                        print("Do all work")
                        print("Pass course")
                        print("Be happy")
                               
                elif h!="1015.txt" and h!="42.txt":
                        print("File not found")
                                
        else:
            x==("x") or x==("X")
            print("Goodbye!")
            break
main()
                    
        
        
            
