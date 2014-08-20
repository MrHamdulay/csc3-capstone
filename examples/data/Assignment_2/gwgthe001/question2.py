#GWGTHE001
#Gwegwana Thembekani
#Program to determine whether you should eat something if you dropped it.
# March 2013
print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')
def eat() :
    eat='Decision: Eat it.'
    dont="Decision: Don't eat it."
    dec='Decision: Your call.'
    q1=input('Did anyone see you? (yes/no) \n')
    if (q1=='yes') :
        q2=input('Was it a boss/lover/parent? (yes/no)\n')
        if (q2=='yes') :
            q3=input('Was it expensive? (yes/no) \n')
            if (q3=='yes') :
                q4=input('Can you cut off the part that touched the floor? (yes/no) \n')
                if (q4=='yes') :
                    print(eat)
                elif (q4=='no') :
                    print(dec)
            elif (q3=='no') :
                qd=input('Is it chocolate? (yes/no) \n')
                if (qd=='yes') :
                    print(eat)
                elif (qd=='no') :
                    print(dont) 
        elif (q2=='no'):
            print(eat)
    elif (q1=='no') :
        qa=input('Was it sticky? (yes/no) \n')
        if (qa=='yes') :
            qb=input('Is it a raw steak? (yes/no) \n')
            if (qb=='yes') :
                qc=input('Are you a puma? (yes/no) \n')
                if (qc=='yes') :
                        print(eat)
                elif (qc=='no') :
                    print(dont)
            elif (qb=='no') :
                    qe=input('Did the cat lick it? (yes/no) \n')
                    if (qe=='no') :
                        print(eat)
                    elif(qe=='yes') :
                        qf=input('Is your cat healthy? (yes/no) \n')
                        if (qf=='yes') :
                            print(eat)
                        elif (qf=='no') :
                            print(dec)
        elif (qa=='no'):
            qg=input('Is it an Emausaurus? (yes/no) \n')
            if (qg=='yes') :
                qh=input('Are you a Megalosaurus? (yes/no) \n')
                if (qh=='yes') :
                    print(eat)
                elif (qh=='no') :
                    print(dont)
            elif (qg=='no') :
                qi=input('Did the cat lick it? (yes/no) \n')
                if (qi=='yes') :
                    qj=input('Is your cat healthy? (yes/no) \n')
                    if (qj=='yes') :
                        print(eat)  
                    elif (qj=='no') :
                        print(dec)
                elif (qi=='no') :
                    print(eat)
                    
                    
            

                        
    
                               
       
    
                
        
               
               
eat()