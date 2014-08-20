'''BBS program,rory welsh,wlsror002'''

#replaces old message with new
def enter():
    new_message= input("Enter the message:\n")
    return new_message

#select file and display selected file content
def display():
    x=input('Enter the filename:\n')
    if x=='42.txt':
        print('The meaning of life is blah blah blah ...')
    elif x== '1015.txt':
        print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
    else:
        print("File not found")

#display menu with selection options
def main(x):
    Message= 'no message yet'
    
    if x== 'E' or x=='e':
        New_Message=enter()
        Message=New_Message
        
    elif x== 'V' or x=='v':
        print('The message is:',Message)
    elif x=='L' or x=='l':
        print('List of files: ',file_1,', ',file_2,sep='')
    elif x=='D' or x=='d':
        display()

#loop functions until told to stop
while 'true':
    file_1='42.txt' 
    file_2='1015.txt'
    x= input("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it\nEnter your selection:\n")        
    main(x)
    if x =='X' or x=='x':
        print('Goodbye!')
        break
        








