height = eval(input("Enter the height of the triangle:\n"))
space =height-1
for i in range (1,height+height+1,2):
    if(space <= 0):
        print("*"*i)
    else:
        print (" "*(space-1),"*"*i)
        space -= 1        
        
    


    
              
              