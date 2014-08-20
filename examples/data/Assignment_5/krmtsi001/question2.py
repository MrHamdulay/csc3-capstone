#This program to stimulate a vending machine and calculate change based on the amount paid.
#Tsitsi Karimakwenda
#20 April 2014

cost=eval(input("Enter the cost (in cents): \n")) #the string number is changed into a python number
deposit = 0
if cost!=0: #this is a condition that states if cost is not equals to zero then you should carryon with the while loop

    while deposit<cost: 
        inputd=eval(input("Deposit a coin or note (in cents):\n")) #inside the while loop when the deposite number is lower than the cost you keep asking the deposite number
        deposit+=inputd
    
  #change has to be in the loop until deposit is bigger than the cost and it is in this line because change needs to be defined first

    change=deposit-cost#the intial change is stated and it goes through the conditions that keep changing the chage statement less and less with every if until all the change has been converted to the display option
    if change!=0:
        print("Your change is:") 
        i=1
        if change >=100:
            i=change//100
            print(i,"x $1")
            change=change-(100*i)
          
                     
                     
        if change >=25:
            i=change//25
            print(i,"x 25c")
            change=change-(25*i)
                
        if change >=10:
            i=change//10
            print(i,"x 10c")
            change=change-(10*i) 
            
        if change >=5:
            i=change//5
            print(i,"x 5c")
            change=change-(5*i)   
                
        if change >=1:
            i=change//1
            print(i,"x 1c")
            change=change-(1*i) 
        
        
            
    
            
             
                
           
                
                             
                
                