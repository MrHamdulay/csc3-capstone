#a program to simulate a vending machine
#F.Chigwaza
#17 april 2014


def vending_machine():
    c=eval(input('Enter the cost (in cents):\n'))
     
    if c>0:
        dep=eval(input('Deposit a coin or note (in cents):\n'))
        while dep<c:
            depo=eval(input('Deposit a coin or note (in cents):\n'))
            dep=depo+dep
            
        change=dep-c
           
        if change>0:
                print('Your change is:')
                l=change//100
                if l>0:
                    print(l,'x $1')
                m=change%100
                if m>0:
                    n=m//25
                    if n>0:
                        print(n,'x 25c')
                    o=m%25
                    if o>0:
                        p=o//10
                        if p>0:
                            print(p,'x 10c')
                        q=o%10
                        if q>0:
                            r=q//5
                            if r>0:
                                print(r,'x 5c')
                            s=q%5
                            if s>0:
                                t=s//1
                                if t>0:
                                    print(t,'x 1c')
                                            
                                            
vending_machine()                                            
                                        
                                    
                                      
                                
                       
    
        
    