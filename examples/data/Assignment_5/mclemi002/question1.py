#Emile McLennan
#Q1
#14/4/14
files=["The meaning of life is blah blah blah ...","Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy"]
choice=''
f1=False
f2=False
msg='no message yet'
while choice != 'X':
    print("Welcome to UCT BBS\nMENU")
    choice=(input("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")).upper()    
    if choice == 'E':
        msg= input("Enter the message:\n")
    if choice=='V':
        print('The message is:',msg)
    if choice=='X':
        print("Goodbye!")
        break
    if choice=='D':
        fname=input("Enter the filename:\n")
        if fname=="42.txt":
            print("The meaning of life is blah blah blah ...")
            #del files[0]
            f1= True
        if fname=="1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            f2=True
        if fname !='42.txt' and fname != '1015.txt':
            print('File not found')

    if choice =='L':
        if f1 ==False and f2 ==False:
            print('List of files: 42.txt, 1015.txt')
        if f1 == True and f2 ==False:
            print('List of files: 1015.txt')
        if f1==False and f2 ==True:
            print('List of files: 42.txt')
        if f1==True and f2==True:
            print('File not found')
        
        
            