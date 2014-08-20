def desicion():

    a='Did anyone see you? (yes/no)\n'
    b='Was it a boss/lover/parent? (yes/no)\n' 
    c='Was it expensive? (yes/no)\n'
    d='Is it chocolate? (yes/no)\n'
    e='Can you cut off the part that touched the floor? (yes/no)\n'
    f='Was it sticky? (yes/no)\n' 
    g='Is it an Emausaurus? (yes/no)\n' 
    h='Is it a raw steak? (yes/no)\n' 
    i='Are you a Megalosaurus? (yes/no)\n'
    j='Did the cat lick it? (yes/no)\n'
    k='Are you a puma? (yes/no)\n'
    l='Is your cat healthy? (yes/no)\n'

   
    if input(a)=='yes':
        if input(b)=='yes':
            if input(c)=='no':
                if input(d)=='no':
                    print("Decision: Don't eat it.")
                else:
                    print('Decision: Eat it.')                    
            else:
                if input(e)=='no':
                    print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
        else:   
            print('Decision: Eat it.')
       
                
    else:             
        if input(f)=='no':
            if input(g)=='yes':
                if input(i)=='yes':
                    print('Decision: Eat it.')
                else:
                    print("Decision: Don't eat it.")
                
            else:
                if input(j)=='yes':
                    if input(l)=='yes':
                        print('Decision: Eat it.')
                    else :
                        print('Decision: Your call.')
                else:
                    print('Decision: Eat it.')
        else:
            if input(h)=='no':
                if input(j)=='yes':
                    if input(l)=='yes':
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
                     
            else:
                if input(k)=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
                    
print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')    
desicion()                    
                
                
                
       
           
            

