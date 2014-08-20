"""Sphiwe Muthembi
Std no: MTHSPH007
 Program to calculate change"""
def calc_change(change):
    
    if change >= 100:
        dollar(change)
    elif 25 <= change < 100:
        twentyfive_cent(change)
    elif 10 <= change < 25:
        ten_cent(change)
    elif 5 <= change < 10:
        five_cent(change)
    elif 1 <= change < 5:
        one_cent(change)

def dollar(x):
    
    count= 0
    i= 100
    while i <= x:
        chng= x-i
        count+=1
        i+=100
    print(count,"x $1")
    calc_change(chng)
       


       
def twentyfive_cent(x):
    count= 0
    i=25
    while x >= i:
        count+=1
        chng= x -i
        i+=25
   
    print(count,"x 25c") 
    if chng > 0:
        
        calc_change(chng)
    
        
    

#calc_change(775)
        
def ten_cent(x):
    count= 0
    i=10
    while x >= i:
        count+=1
        chng= x- i
        i+=10
    print(count,"x 10c")
    calc_change(chng)
    
 
#calc_change(795)    
def five_cent(x):
    count = 0
    i= 5
    while x >=i:
        count+=1
        chng= x- i
        i+=5
    print(count,"x 5c")
    calc_change(chng)
     
 
#calc_change(765) 
    
def one_cent(x):
    count = 0
    i= 1
    while x >=i:
        count+=1
        chng= x- i
        i+=1
    print(count,"x 1c")
    calc_change(chng)
      
    


#inputs


def inputs():
    cont= True
    cost= eval(input("Enter the cost (in cents):\n"))
    if cost == 0:
        cont =False 
    while cont:
        
        
        k = 0
        while k < cost:
            deposit= eval(input("Deposit a coin or note (in cents):\n"))
            k+= deposit
           
          
        change = k - cost
        if change >0:
            print("Your change is:") 
            calc_change(change)

        cont = False
   
        
            
inputs()    
            
        
    