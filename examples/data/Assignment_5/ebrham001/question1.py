'''Program simulating Bulletin Board System
HAMZA EBRAHIM
17/04/14'''

# defining text file functions

def txtFour():
        F = 'The meaning of life is blah blah blah ...'
        return F
    
def txtTen():
        T = 'Computer Science class notes ... simplified\n''Do all work\n''Pass course\n''Be happy'
        return T
    
def txtSix():
        S = 'File not found'
        return S    


# defining BBS function - main function
   
def BBS():
        
        # select and store variables created
        
        select = 'start'
        store = 'no message yet'         

        
        # string manipulation to identify which option has been selected
        
        # while loop so they program knows to continue running and prompt for more input
        
        while select[0] != 'x' or select[0] != 'X':
                
                # print welcome message
                print('Welcome to UCT BBS')
                print('MENU')
                print('(E)nter a message')
                print('(V)iew message')
                print('(L)ist files')
                print('(D)isplay file')
                print('e(X)it')    
        
                # text file functions assigned variables within main function
        
                z = txtFour()
                w = txtTen()
                j = txtSix()
        
                
                # asks for user input 
                
                # string manipulation to identify which option has been selected
        
                select = input("Enter your selection:\n")
                
                
                if select[0] == 'e' or select[0]== 'E':
                        store = input("Enter the message:\n")
                
       
                if select[0] == 'v' or select == 'V':
                        print('The message is:', store)
                       
                        
                
                
    
                if select[0] == 'l' or select[0] == 'L':
                        print('List of files:', '42.txt,', '1015.txt')
                
    
            
                if select[0] =='d' or select[0] == 'D':
                        ans = input("Enter the filename:\n")
                        
                        # string manipulation to identify which text file to reproduce
                        
                        if ans[0] == '4':
                                print(z)
                        
                        elif ans[3] == '5':
                                print(w)
                        
                        elif ans[3] != 't' or '5':
                                print(j)
                                
                # program ends when this input is given - break prevents loop back to top 
                if select[0] == 'x' or select == 'X':
                        print('Goodbye!')                                
                        break
                     
                        
# program ends                        
                        
BBS()                        