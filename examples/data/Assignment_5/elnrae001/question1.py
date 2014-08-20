'''Text-based program, a simple BBS
Author: Raees Eland
Date: 15 April 2014'''
    
def BBS():
    choice=''
    while choice!='X':
        print('Welcome to UCT BBS','MENU','(E)nter a message','(V)iew message','(L)ist files','(D)isplay file','e(X)it',sep='\n')
        choice=input('Enter your selection:\n')
        choice=choice.upper()
        

        if choice=='E':
            # executes the loop until there is no message
            while choice=='E':
                e=input('Enter the message:\n')
                print('Welcome to UCT BBS','MENU','(E)nter a message','(V)iew message','(L)ist files','(D)isplay file','e(X)it',sep='\n')
                choice=input('Enter your selection:\n')
                choice=choice.upper()
                if choice=='V': # will only execute while choice is E
                    print('The message is:',e)
                    break        

        elif choice=='V':
            print('The message is: no message yet')
        elif choice=='X':
            print('Goodbye!')
            break
        elif choice=='L':
            print('List of files: 42.txt, 1015.txt')
        elif choice=='D':
            d=input('Enter the filename:\n')
            if d=='42.txt':
                print('The meaning of life is blah blah blah ...')
            elif d== '1015.txt':
                print('Computer Science class notes ... simplified','Do all work','Pass course','Be happy',sep='\n')
            else:
                print('File not found')
                
if __name__ == '__main__':
    BBS()



    

    

