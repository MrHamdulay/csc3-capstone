#Sample BBM
#James Godlonton
#12 April 2014

file = open("1015.txt", "w");
file.write("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy");
file.close();
    
file2 = open("42.txt", "w");
file2.write("The meaning of life is blah blah blah ...")
file2.close()

def menu():

    message="no message yet"
    while True:
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
        choice=input("Enter your selection:\n")
        choice=choice.upper()
        if choice=='X':
            print("Goodbye!")
            break
        elif choice=='E':
            message=input("Enter the message:\n")
            
        elif choice=='V':
            print("The message is: "+message)
            
        elif choice=='L':
            print("List of files: 42.txt, 1015.txt")
           
        elif choice=='D':
            fil=input("Enter the filename:\n")
            try:
                x=open(fil,"r")
                print (x.read())
            except (OSError, IOError) as e:
                print("File not found")
        






    
if __name__ == "__main__":
    menu()