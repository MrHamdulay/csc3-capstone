#Vending Machine
#James Godlonton
#12 April 2014

def menu():
    ans= eval(input("Enter the cost (in cents):\n"))
    paid=0
    while paid<ans:
        paid=paid+eval(input("Deposit a coin or note (in cents):\n"))
    change=paid-ans
   
    if(paid==ans):
        print("",end="")
        
    else:
        print("Your change is:")
        c100=(change-change%100)//100        
        if(c100>=1):
            print(str(c100)+" x $1")
        change=change%100
    
        c25=(change-change%25)//25
        if(c25>=1):
            print(str(c25)+" x 25c")
        change=change%25
    
        c10=(change-change%10)//10
        if(c10>=1):
            print(str(c10)+" x 10c")
        change=change%10
    
        c5=(change-change%5)//5
        if(c5>=1):
            print(str(c5)+" x 5c")
        change=change%5
    
    
        if(change>=1):
            print(str(change)+" x 1c")
        change=0    
    


        
        
        
    


    
    
if __name__ == "__main__":
    menu()