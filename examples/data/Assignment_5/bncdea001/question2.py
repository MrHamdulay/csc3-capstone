#Assignment 5 Question 2
# Change counter
#Dean Bunce
#14 April 2014



def main():
    #Get cost
    cost=eval(input("Enter the cost (in cents): \n"))
    #Set amount paid to 0
    paid=0
    #Keep asking for change until the amount is paid
    while paid<=cost:
        if paid==cost:break
        cashin=eval(input("Deposit a coin or note (in cents):\n"))
        paid+=cashin
    
    
    
    else:
        #Set change
        change=paid-cost
        #Creat options and split them
        options="25,10,5,1"
        options=options.split(",")
        print("Your change is:")
        
        #For great than a dollar
        if (change//100)>0:
            dollar=change//100
            change=change-dollar*100
            print(dollar, "x", "$1")
            
        #Sort through change increments in decreasing order until change is paid
        for i in options:
            each=change//int(i)
            if each>0:
                print(each, "x", i+"c")
                change=change-int(i)*each
            if change-int(i)*each==0: break
            else:continue
            
       

main()
