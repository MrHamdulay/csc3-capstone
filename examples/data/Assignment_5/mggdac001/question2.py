


def mach():
    cost=eval(input('Enter the cost (in cents):\n'))
    
    if cost!=0:
        dep=eval(input('Deposit a coin or note (in cents):\n'))
        
        #change=dep-cost
        answer="yes"
       
    
        while dep<cost:
            s=eval(input('Deposit a coin or note (in cents):\n'))
            dep+=s
        
        change=dep-cost
        length=len(str(change))
        if dep>cost:
            print('Your change is:')
           
        if length>=3:
           
            n=0
            while change >=100:
                change-=100
                n+=1

            print(n,"x","$1")
            if change>=25:
                n=0
                while change>=25:
                    change-=25
                    n+=1
                print(n,'x',"25c")
                if change>=10:
                    n=0
                    while change>=10:
                        change-=10
                        n+=1
                    print(n,'x','10c')
                    if change>=5:
                        n=0
                        while change>=5:
                            change-=5
                            n+=1
                        print(n,'x','5c')
                        if change>=1:
                            n=0
                            while change>=1:
                                change-=1
                                n+=1
                            print(n,'x','1c') 
                    elif change>=1:
                        n=0
                        while change>=1:
                            change-=1
                            n+=1
                        print(n,'x','1c')                             
                    
                elif change>=5:
                    n=0
                    while change>=5:
                        change-=5
                        n+=1
                    print(n,'x','5c')
                    if change>=1:
                        n=0
                        while change>=1:
                            change-=1
                            n+=1
                        print(n,'x','1c') 
                elif change>=1:
                    n=0
                    while change>=1:
                        change-=1
                        n+=1
                        print(n,'x','1c')                        
            elif change>=10:
                
                n=0
                while change>=10:
                    change-=10
                    n+=1
                print(n,'x','10c')
                if change>=5:
                    n=0
                    while change>=5:
                        change-=5
                        n+=1
                    print(n,'x','5c')
                    if change>=1:
                        n=0
                        while change>=1:
                            change-=1
                            n+=1
                        print(n,'x','1c') 
                elif change>=1:
                    n=0
                    while change>=1:
                        change-=1
                        n+=1
                    print(n,'x','1c')                             
                
            elif change>=5:
                n=0
                while change>=5:
                    change-=5
                    n+=1
                print(n,'x','5c')
                if change>=1:
                    n=0
                    while change>=1:
                        change-=1
                        n+=1
                    print(n,'x','1c') 
            elif change>=1:
                n=0
                while change>=1:
                    change-=1
                    n+=1
                    print(n,'x','1c')                  
                       
        elif length!=3:
            if change>=25:
                n=0
                while change>=25:
                    change-=25
                    n+=1
                print(n,'x',"25c")
                if change>=10:
                    n=0
                    while change>=10:
                        change-=10
                        n+=1
                    print(n,'x','10c')
                    if change>=5:
                        n=0
                        while change>=5:
                            change-=5
                            n+=1
                        print(n,'x','5c')
                        if change>=1:
                            n=0
                            while change>=1:
                                change-=1
                                n+=1
                            print(n,'x','1c') 
                    elif change>=1:
                        n=0
                        while change>=1:
                            change-=1
                            n+=1
                        print(n,'x','1c')                             
                    
                elif change>=5:
                    n=0
                    while change>=5:
                        change-=5
                        n+=1
                    print(n,'x','5c')
                    if change>=1:
                        n=0
                        while change>=1:
                            change-=1
                            n+=1
                        print(n,'x','1c') 
                elif change>=1:
                    n=0
                    while change>=1:
                        change-=1
                        n+=1
                        print(n,'x','1c')                        
            elif change>=10:
                
                n=0
                while change>=10:
                    change-=10
                    n+=1
                print(n,'x','10c')
                if change>=5:
                    n=0
                    while change>=5:
                        change-=5
                        n+=1
                    print(n,'x','5c')
                    if change>=1:
                        n=0
                        while change>=1:
                            change-=1
                            n+=1
                        print(n,'x','1c') 
                elif change>=1:
                    n=0
                    while change>=1:
                        change-=1
                        n+=1
                    print(n,'x','1c')                             
                
            elif change>=5:
                n=0
                while change>=5:
                    change-=5
                    n+=1
                print(n,'x','5c')
                if change>=1:
                    n=0
                    while change>=1:
                        change-=1
                        n+=1
                    print(n,'x','1c') 
            elif change>=1:
                n=0
                while change>=1:
                    change-=1
                    n+=1
                print(n,'x','1c')                     

          



    
        #elif length==1:
          
            #n=0
            #while change>=5:
                #change-=5
                #n+=1
            #print(n,'x','5c')
        #elif change>=1:
            #n=0
            #while change>=1:
                #change-=1
                #n+=1
            #print(n,'x','1c')             

            
            
          
    
   
    
            
      
        
mach()