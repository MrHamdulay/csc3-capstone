#Phumelele Ndimande
#Assignment 5

def main():
    
    menu= "Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it"
    print(menu) #print menu
    
main()
#enter the selection
x= input("Enter your selection:\n")
message="no message yet"
#selections
while x.upper() != 'X':
    if x.upper()== 'E':
        message = input("Enter the message:\n")
    if x.upper() == 'V':
            print("The message is:", message)
    
    if x.upper() == 'L':
        print("List of files: 42.txt, 1015.txt")

    if x.upper() == 'D':
            f= input("Enter the filename:\n")
            if f == '42.txt':
                print("The meaning of life is blah blah blah ...")
            elif f == '1015.txt':
                print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            else:
                print("File not found")
                 
    main()
    x= input("Enter your selection:\n")
    
if x.upper()== 'X':
            print("Goodbye!")
        

