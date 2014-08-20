#assignment5 q1, prog for bulletin board systems


#function for the available selections
def pre():
            print ('Welcome to UCT BBS')
            print ('MENU')
            print ('(E)nter a message')
            print ('(V)iew message')
            print ('(L)ist files')
            print ('(D)isplay file')
            print ('e(X)it') 
#function for calculating the change            
def bbs():
            pre()
            #get selection from the user 
            selec = input('Enter your selection:\n')
            #for the selections which are not x, execute the following code 
            while selec != 'X' or selec !='x':
                        #if selection is e then ask user to enter a message 
                        if selec=='E' or selec=='e':
                                    mess = input('Enter the message:\n')
                                    pre()
                                    selec = input('Enter your selection:\n')
                                  # if the selction after entering the message 
                                  #is v display the message previously typed 
                                    if selec=='V' or selec=='v':
                                                print('The message is: '+mess)  
                                                pre()
                                                selec = input('Enter your selection:\n')
                                                
                        #if the selection is v without the user entering a message display the default message                        
                        if selec=='V' or selec=='v':
                                                print('The message is: no message yet')  
                                                pre()
                                                selec = input('Enter your selection:\n')
                        
                                    
                     
                        #if selection is l then list the availabe files
                        elif selec=='L' or selec=='l':
                                    print('List of files: 42.txt, 1015.txt')
                                    pre()
                                    selec = input('Enter your selection:\n')
                        #if selection is d diplay the files in accordance to the name which is entered by the user
                        elif selec=='D' or selec=='d':
                                    file_name=input('Enter the filename:\n')
                                    
                                    if file_name=='42.txt':
                                                print('The meaning of life is blah blah blah ...')
                                                pre()
                                                selec = input('Enter your selection:\n')
                                    elif file_name=='1015.txt':
                                                print('Computer Science class notes ... simplified')
                                                print('Do all work')
                                                print('Pass course')
                                                print('Be happy')
                                                pre()
                                                selec = input('Enter your selection:\n')
                                    else:
                                                print('File not found')
                                                pre()
                                                selec = input('Enter your selection:\n')
                        #if selcection is x the display goodbye and quit the program
                        elif selec=='X' or selec=='x':
                                    print('Goodbye!')
                                    break

                                    
bbs()