# Programme to simulate a simple BBS with one stored message and 2 fixed files
# Wongwa Giqwa
# 14 April 2014


# Function to display welcome
def display():
    print('Welcome to UCT BBS')
# Function to display options    
def menu():
    print('MENU')
    print('(E)nter a message')
    print('(V)iew message')
    print('(L)ist files')
    print('(D)isplay file')
    print('e(X)it')

# Function to run diiferent options/selections    
def main():
    
    message=str('no message yet')
    while True:
        display()
        menu()
        selection=input('Enter your selection:\n')
       
        if selection=='E' or selection =='e':
            message=[]
            message=input('Enter the message:\n')
            
            
        if selection=='V' or selection == 'v':
            
            print('The message is:',message)
        
            
                
        if selection=='L' or selection =='l':
            print('List of files: 42.txt, 1015.txt')
        if selection=='D' or selection =='d':
            print('Enter the filename:')
            file=input()
            if file=='42.txt':
                print('The meaning of life is blah blah blah ...')
            elif file=='1015.txt':
                    print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
            else:
                print('File not found')
        if selection=='X' or selection =='x':
            print('Goodbye!')
            break
            
            
                
            
            
            
            
main()
           
            
        
        
    
    
    