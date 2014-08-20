# Program acting as a small BBS for UCT
# Written by Lwazi Shezi
# 14.04.2014

print('Welcome to UCT BBS')
print('MENU')
print('(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')

selection=input('Enter your selection:\n') 
real_selection=selection.lower() # Ensuring that all input whether upper case or lower will be accepted

while real_selection != 'x': 
    if real_selection == 'e':
        test_message = input('Enter the message\n')
        
    elif real_selection == 'v':
        if test_message:
            print('The message is:',test_message)
        
    elif real_selection == 'l':
        print('List of files: 42.txt, 1015.txt')
        
    else:
        if real_selection == 'd':
            file_name=input('Enter the filename:\n')
            
            if file_name == '42.txt':
                print('The meaning of life is blah blah blah ...')
                
            elif file_name == '1015.txt':
                print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
                
            else: print('File not found')
    
    print('Welcome to UCT BBS')
    print('MENU')
    print('(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
            
    selection=input('Enter your selection:\n')
    real_selection=selection.lower()            
            
if real_selection == 'x':
    print('Goodbye!')
    

