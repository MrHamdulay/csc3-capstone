"""Sibulele Hlongwane
Date: 13 April 2014
Vending Machine simulation"""

deposit=0
cost= eval(input("Enter the cost (in cents):\n"))
#Keep asking user to deposit money if does not meet cost
while deposit<cost:
    deposit= deposit+ eval(input("Deposit a coin or note (in cents):\n"))
change= deposit-cost

#If change is greater than 100
if change>100:
    changedollars=change//100               
    print("Your change is:\n" + str(changedollars), "x $1")
    smallchange=change-changedollars*100
  
   #Division of small change(which is less than 100) into seperate components depending on what its divisible by
   
    if smallchange>0:                         
        change25=smallchange/25                        
        changeint25= smallchange//25           
        if change25>=1:
            print(str(changeint25), "x 25c")
            smallchange= smallchange-(changeint25*25)  
            change10= smallchange/10     
            changeint10=smallchange//10   
            if change10>=1:
                print(str(changeint10), "x 10c")              
                smallchange= smallchange-(changeint10*10) 
                change5= smallchange/5            
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change1>0:
                        print(str(changeint1), "x 1c")                

            else:
                change5= smallchange/5          
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")                    
                    
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change1>0:
                        print(str(changeint1), "x 1c")
                
    if change25<1:
            change10=smallchange/10
            changeint10=smallchange//25
            change10= smallchange/10    
            changeint10=smallchange//10    
            if change10>=1:
                print(str(changeint10), "x 10c")              
                smallchange= smallchange-(changeint10*10) 
                change5= smallchange/5         
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change1>0:
                        print(str(changeint1), "x 1c")                

            else:
                change5= smallchange/5         
                changeint5=smallchange//5   
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")          
                else:
                    change1=smallchange/1                
                    changeint1=smallchange//1 
                    if change1>0:
                        print(str(changeint1), "x 1c")
#if change is smaller than 100: code similar to above
if change<100:               
 
    smallchange=change #as change is smaller than 100
   #Division of small change(which is less than 100) into seperate components depending on what its divisible by
    if smallchange>0:   
        print("Your change is:")
        change25=smallchange/25                      
        changeint25= smallchange//25          
        if change25>=1:
            print(str(changeint25), "x 25c")
            smallchange= smallchange-(changeint25*25)   
            change10= smallchange/10     
            changeint10=smallchange//10  
            if change10>=1:
                print(str(changeint10), "x 10c")              
                smallchange= smallchange-(changeint10*10) 
                change5= smallchange/5      
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change1>1:
                        print(str(changeint1), "x 1c")                

            else:
                change5= smallchange/5         
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
                    
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change1>1:
                        print(str(changeint1), "x 1c")
                
        if change25<1:
            change10=smallchange/10
            changeint10=smallchange//25
            change10= smallchange/10    
            changeint10=smallchange//10    
            if change10>=1:
                print(str(changeint10), "x 10c")              
                smallchange= smallchange-(changeint10*10) 
                change5= smallchange/5         
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change1>1:
                        print(str(changeint1), "x 1c")                

            else:
                change5= smallchange/5           
                changeint5=smallchange//5
                if change5>=1:
                    print(str(changeint5), "x 5c")
                    smallchange= smallchange-(changeint5*5)
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
                    
                else:
                    change1=smallchange/1
                    changeint1=smallchange//1
                    if change>1:
                        print(str(changeint1), "x 1c")
            
            