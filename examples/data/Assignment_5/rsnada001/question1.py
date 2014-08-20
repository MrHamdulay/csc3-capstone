#Question 1
#Adam Rosendorff-RSNADA001
#15/04/2014

message = 'no message yet'
end = False
files = {'42.txt':'The meaning of life is blah blah blah ...','1015.txt':'''Computer Science class notes ... simplified
Do all work
Pass course
Be happy'''}

def set_message():
    global message
    message = input('Enter the message:\n')

def get_message():
    print('The message is:',message)

def list_files():
    print('List of files: ',list(files.keys())[0],', ',list(files.keys())[1],sep='')

def get_file():
    file = input('Enter the filename:\n')
    if file in files:
        print(files[file])
    else:
        print('File not found')

def stop():
    global end
    end = True
    print('Goodbye!')
    
menu = {'e':set_message,'v':get_message,'l':list_files,'d':get_file,'x':stop}
while (end == False):
    print('''Welcome to UCT BBS
MENU
(E)nter a message
(V)iew message
(L)ist files
(D)isplay file
e(X)it
Enter your selection:''')
    selection = input()
    menu[selection.lower()]()
