# Simple BBS
# Irfan Habib
# 2014/04/16



def structure():
    #print heading and menu
    print('Welcome to UCT BBS\nMENU')
    print('(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it')
       
        
    

def main():
    #build file list
    list1 = ['42.txt','1015.txt']
    
    message = 'no message yet'
    while "fuck_you_don't_look_at_my_code":
            
        structure()
        # get user's choice
        sel = input('Enter your selection:\n').upper()    
        
        if sel=='E':
            message = input('Enter the message:\n')
        elif sel=='V':
            print('The message is:',message)
        elif sel=="L":
            print('List of files: ' +list1[0]+', '+ list1[1])
        elif sel=='D':
            file =input("Enter the filename:\n")
            if file not in list1:
                print("File not found")
            else:
                if file == list1[0]: 
                    print('The meaning of life is blah blah blah ...')
                else:
                    print('Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy')
                   
    
        if sel.upper()=="X":
            print("Goodbye!")
            break
main()