'''program to simulate a BBS system
Wandile Khowa
15-04-2014
'''
ans = ''
msg = 'no message yet'
while ans != 'x':
    print("Welcome to UCT BBS")
    print("MENU")
    print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
    ans = input("Enter your selection: \n")  
    
    def display(): #display function to display files
            file = input("Enter the filename: \n")
            if file == '42.txt':
                print("The meaning of life is blah blah blah ...")
            elif file == '1015.txt':
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
                
    def listi():
        file1 = '42.txt'
        file2 = '1015.txt'
        print("List of files: ", end='')
        print(file1,file2, sep =', ')
    
    if ans.lower() == 'e':
        msg = input("Enter the message: \n") 
                    
    if ans.lower() == 'v':
        print("The message is:", msg)
        
    if ans.lower() == 'd':
        display()
                
    if ans.lower() == 'l':
        listi()    
        
else:
    print("Goodbye!")