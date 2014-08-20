'''Programs that simulates BBS 
 Name: Othniel KONAN
 Student number: KNNOTH001
 Date: 2014/04/12'''

#definition of global variable
message = "no message yet"
i = True 
files=['42.txt','1015.txt']

#function to print the menu and to prompt the user
def menu():
    print('Welcome to UCT BBS\nMENU')
    print('(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:')
#function that return the lower-case of a string input 
def prompt():
    choice = input()
    return choice.lower()

#function that executes instructions according to the input of the user
def choice(ans):
    global message
    global i
    if ans == 'e':
        message = input('Enter the message:\n')
    elif ans == 'v':
        print('The message is:',message)
    elif ans == 'l':
        print('List of files: ',files[0],', ',files[1],sep='')   
    elif ans == 'd':
        file=input('Enter the filename:\n')
        if file == '42.txt':
            print('The meaning of life is blah blah blah ...')
        elif file == '1015.txt':
            print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
        else:
            print('File not found')
    else:
        i = False

#main function of the program  
def main():
    global i
    while i:
        menu()
        ans = prompt()
        choice(ans)
    print('Goodbye!')
    
if __name__ == "__main__":
    main()
