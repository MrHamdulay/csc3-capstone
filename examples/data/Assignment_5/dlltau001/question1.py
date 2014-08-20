#Create a BBS Menu

entry = ''
message = 'no message yet'
files = ["42.txt","1015.txt"]
x = 1
while x:
    print("Welcome to UCT BBS\nMENU")
    print("(E)nter a message")
    print("(V)iew message")
    print("(L)ist files")
    print("(D)isplay file")
    print("e(X)it")
    
    entry = input("Enter your selection:\n")
    
    if entry in 'E,e':
        message = input("Enter the message:\n")
    elif entry in 'V,v':
        print("The message is: ",message,sep="")
    elif entry in 'L,l':
        print("List of files: ",files[0],", ",files[1],sep='')
    elif entry in 'D,d':       
        filename = input("Enter the filename:\n")
        if filename == files[0]:
            print("The meaning of life is blah blah blah ...")
        elif filename == files[1]:
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
        else:
            print("File not found")
    elif entry in 'x,X':
        break
    else: print("File not found")
    
print("Goodbye!")       
        
        