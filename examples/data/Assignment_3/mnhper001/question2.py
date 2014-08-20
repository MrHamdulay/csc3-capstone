def main():
    height=eval(input("Enter the height of the triangle:\n"))
    space=height-1
    base = (height*2) -1
    for i in range(1,base+2,2):
        print(" "*space,end = "")
        print("*"*i)
        space=space-1
main()
        
        
        
        
         
        
        
        
            
            
            
            
            
