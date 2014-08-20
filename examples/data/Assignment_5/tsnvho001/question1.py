#Program to simulate a simple BBS
#Tsanwani Vhonani
#16 April 2014

#function to print the BBS optins
def menu():
    print("Welcome to UCT BBS")
    print("MENU")
    list1=["(E)nter a message","(V)iew message","(L)ist files","(D)isplay file","e(X)it"]
    for a in list1:
        print(a)

#Program to stimulate BBS    
def BBS():
    exit='x'
    view='v'
    enter='e'
    display='d'
    List='l'
    file1='1015.txt'
    file2='42.txt'
    default_mes='no message yet'
    
    menu() #Calling function menu
    select=input('Enter your selection:\n')
    if select==enter:
        message=input('Enter the message:\n')
        menu()
        select=input('Enter your selection:\n')
        if select==view:
            print('The message is:',message)
            menu()
            select=input('Enter your selection:\n')
            if select==exit:
                print('Goodbye!')
   
    elif select==exit:
        print('Goodbye!')
    
    elif select==List:
        print('List of files:',file2+',',file1 )
        for i in range(0,3):
            menu()
            select=input('Enter your selection:\n')
            if select==display:
                ent=input('Enter the filename:\n')
                if ent==file1:
                    print("Computer Science class notes ... simplified")
                    print("Do all work")
                    print("Pass course")
                    print("Be happy")   
                elif ent==file2:
                    print("The meaning of life is blah blah blah ...")
                else:
                    print('File not found')
        menu()
        select=input('Enter your selection:\n')        
        if select==exit:
            print('Goodbye!')
   
    else:  
        print('The message is:',default_mes)
        menu()
        select=input('Enter your selection:\n')
        if select==enter:
            message=input('Enter the message:\n')
            menu()
            select=input('Enter your selection:\n')
            if select==view:
                    print('The message is:',message)
                    menu()
                    select=input('Enter your selection:\n')
                    if select==exit:
                        print('Goodbye!') 
   
            
                                        
BBS() # Call function BBS
        
    