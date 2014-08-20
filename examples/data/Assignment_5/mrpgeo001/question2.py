"""Vending Machine (Change Calculator)
Geoff Murphy
MRPGEO001
13 April 2014"""

def Vend():
    cost = eval(input("Enter the cost (in cents):\n"))      #The total amount to be paid
    pay = 0                                                 #'pay' is amount of money deposited
    
    dollar = 0                                              #Initial values for the 'number' of certain denominations. e.g., ?? x 25c etc.
    c25 = 0
    c10 = 0
    c5 = 0
    c1 = 0
    
    while pay < cost:
        money = eval(input("Deposit a coin or note (in cents):\n")) #continues until full amount is paid or exceeded.
        pay += money
    else:
        
        change = pay - cost                                         #Calculates the change to be given
        change2 = str(change)
        
        if len(change2) > 2:              #Starting counting from the right, if the amount has more than 2 digits, everything after is dollars. e.g., 1250 will have 12 dollars total.
            dollar += eval(change2[:-2])     
        
        
        twentyfive = eval(change2[-2:])                             #Takes the last 2 digits, which will all be cents. e.g., 1250 becomes 50...
        floor = twentyfive//25                                      #Floor divides this value by the current denomination
        if floor != 0:                                              #And as long as it is not equal to 0, i.e. paid up, continues...
            c25 += floor                                            #Takes this result and adds it to the 'number' of denominations...
            twentyfive -= (floor*25)                                #And then takes this value again, multiplies it by the denomination (i.e. 25 here), and subtracts it from the 
                                                                    #current total (twentyfive).
            
        ten = twentyfive                                            #The current total is renamed 'ten', and the same procedure is followed as before.
        floor2 = ten//10
        if floor2 != 0:
            c10 += floor2
            ten -= (floor2*10)
            
        five = ten
        floor3 = five//5
        if floor3 != 0:
            c5 += floor3
            five -= (floor3*5)
        
        
        one = five
        floor4 = one//1
        if floor4 != 0:
            c1 += floor4
            one -= (floor4*1)
             
        
        if change != 0:                                             #So long as the change is not zero, the denominations multiplied by their numbers will be printed out.
            print("Your change is:")
        if dollar > 0:
            print(dollar, "x $1")
        if c25 > 0:
            print(c25,"x 25c")
        if c10 > 0:
            print(c10,"x 10c")
        if c5 > 0:
            print(c5, "x 5c")
        if c1 > 0:
            print(c1, "x 1c")
        
            
        
Vend()