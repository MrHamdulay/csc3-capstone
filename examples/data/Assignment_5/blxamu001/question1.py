"""Program to act as BBS 

Name: Aubrey Baloi

Student number: BLXAMU001

Date: 15-April-2014"""


def main():
    
    amu = True
    message = ''
    
    while amu:
        
        print('Welcome to UCT BBS')
        print('MENU')
        print('(E)nter a message')
        print('(V)iew message')
        print('(L)ist files')
        print('(D)isplay file')
        print('e(X)it')
        
        choice = input('Enter your selection:\n')
        choice = choice.upper()
        
        if choice in 'E':
            
            message = input('Enter the message:\n')
            
            
        if choice in 'V':
            
            if bool(message) == False:
                print('The message is: no message yet')
            else:
                print('The message is: '+message)
        
        elif choice in 'L':
            
            print('List of files: 42.txt, 1015.txt')
        
        elif choice in 'D':
            
            file_name = (input('Enter the filename:\n'))
            
            if file_name == '42.txt':
                
                print('The meaning of life is blah blah blah ...')
            
            elif file_name == '1015.txt':
                
                print('Computer Science class notes ... simplified')
                print('Do all work')
                print('Pass course')
                print('Be happy')
            
            else:
                print('File not found')
        
        elif choice in 'X':
            
            print('Goodbye!')
            
            amu = False
            
            
            
if __name__=='__main__':
    
    main()
