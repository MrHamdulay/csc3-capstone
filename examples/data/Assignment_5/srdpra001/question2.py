"""
Prashanth Sridharan
SRDPRA001
Question 02
Assignment 5
"""
"""
Variable names being used here"""
#the variable name for cost is c
#variable name for the amount deposited is d
#variable name for the change received/ or the ramining amount to be returned is r
#i is the variable name for the string that is output
#GilStu is the variable name given for the One Dollar change
#quarter is the variable name for the Twenty Five Cents change
#nickel is the variable name for the five cents change

c = eval(input("Enter the cost (in cents):\n")) #step to input the amount

if (c!=0): 
    d=eval(input("Deposit a coin or note (in cents):\n"))
    r = c-d
    
    while (r>0): #This step is only carried out assuming there is change
        d+=eval(input("Deposit a coin or note (in cents):\n"))
        r = c-d
   
    i = str(abs(r)) 
    
    if(eval(i)>0):  #if it exceeds this, the person has recieved excess change
        GilStu="0" 
        if(len(i)>2):
            GilStu = i[:-2] #The number of 1 Dollar bills as change
        cents = eval(i[-2:])
        quarter = cents//25 #The number of 25 cents to be returned
        cents = cents%25 #The change which is deducted
        tenc = cents//10 #The number of ten cents coins to be returned
        cents = cents%10 #The change is which is deducted
        nickel = cents//5 #The number of 5 cents coins to be returned
        cents = cents%5 #The change is which is deducted
        penny = cents//1 #The number of 1 cent coins to be returned
            
        #the output of the change to be returned is listed below.
        print("Your change is:")
        if(eval(GilStu)>0):
            print(GilStu+" x $1")
        if(quarter>0):
            print(quarter,"x 25c")
        if(tenc>0):
            print(tenc,"x 10c")
        if(nickel>0):
            print(nickel,"x 5c") 
        if(penny>0):
            print(penny,"x 1c") 
