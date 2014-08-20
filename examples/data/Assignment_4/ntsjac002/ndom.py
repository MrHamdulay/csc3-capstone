def decimal_to_ndom(a):
    
#changes ndom no to ddecimal
    den=6
    num=a
    num_string=""
    
    statement=True
    
    while statement:
        
            if num >= den:#while a is bigger than denominator
                x=num//den
                y=num%den
                num_string+=str(y)
                num=x
                #print(num_string),#Uncomment it if you want to see what the prigram does every signle tym it runs thru the loop
                #if the 'if' statement is not met or no longer can be met
            else :
                num_string+=str(num)
                statement=False
    return str(num_string)[::-1]

def ndom_to_decimal(a):
     
    
    num=str(a)
    multy=6
    power = len(num)-1
    new_num=0
    

    
    

    for i in num:
    
        #print(int(i)*multy**power)

        x=int(i)*(multy**power)
        new_num+=(x)
        power-=1 #decrease the exponent by 1 after every cycle in the loop
    return(new_num)
                
            
def ndom_add(a,b):
    
    num = 0
    ans = 0
    i = 0
    c = 0
    
    while a != 0:
        num = a%10 + b%10 +c 
        #print(num)
        if num >=6:
            num = num-6
            c=1
            #print(num)
            
        else:
            c=0
        ans += num*10**i
        #print(ans)
        i+=1
        a=a//10
        b=b//10

    return ans

def ndom_multiply(a,b):
    
    num = 0
    ans = 0
    i = 0
    c = 0
       
    while a != 0:
        num = a%10 * b%10 
        print(num)
    
        if num >=6:
            num = num-6
            c=1
            print(num)
               
        else:
            c=0
        ans *= num
        print(ans)
        i+=1
    
        
   
    return ans    



        

    

                
                
                
            
            
            
            
        
            
            
           
            
    