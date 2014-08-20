def txt1015():
    print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
    
def txt42():
    print('The meaning of life is blah blah blah ...')
    
def menu():
    
    print("Welcome to UCT BBS \nMENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    sel = input("Enter your selection:\n")     
    

    mes='no message yet'
    while sel!='X' and sel!='x':
      
        if sel=='E' or sel=='e':
            mes=input("Enter the message:\n")
            
        elif sel=='V'or sel=='v':
            print('The message is:', mes)
        
        elif sel=='L' or sel=='l':
            print('List of files: 42.txt, 1015.txt')
        
        elif sel=='D' or sel=='d':
            fil=input('Enter the filename:\n')
            if fil=='42.txt':
                txt42()
            elif fil=='1015.txt':
                txt1015()
            else:
                print('File not found')
            
        print("Welcome to UCT BBS \nMENU")
        print("(E)nter a message")
        print("(V)iew message")
        print("(L)ist files")
        print("(D)isplay file")
        print("e(X)it")
        sel = input("Enter your selection:\n")          
            
           
    if sel=='X'or sel=='x':
            print('Goodbye!')
        
if __name__=='__main__':
    menu()
          