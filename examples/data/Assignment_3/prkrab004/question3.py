# Assignment 
# Question 3
# PRKRAB004

def box():
    m=input("Enter the message: "'\n')
    r=eval(input("Enter the message repeat count:"'\n'))
    t=eval(input("Enter the frame thickness:" '\n'))
    l='|'*t
    y=len(m)+2
    x= len(m)+t*2 #Length with frame
  
    
    for top in range(t):
        print('|'*top,'+','-'*x,'+','|'*top,sep='')
        x=x-2
        
    for middle in range(r):
        print(l,m,l)
        
    for b in range(t,0,-1):
        print('|'*(b-1),'+','-'*y,'+','|'*(b-1),sep='')
        y=y+2
    
   
   
      
    

box()    