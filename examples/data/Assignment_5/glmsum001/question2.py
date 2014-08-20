#Sumayah Goolam Rassool
#GLMSUM001
#15 April 2014

#---------------------------------------------------user input-------------------------------------------------

cost=eval(input("Enter the cost (in cents):\n"))

if cost>0:
    
    paid=eval(input("Deposit a coin or note (in cents):\n"))




#---------------continues to ask user to enter money until the amount paid is greater than or equal to cost-----

    while paid<cost:
    
        paid+=eval(input("Deposit a coin or note (in cents):\n"))

#---------------------------------------------calculate change due----------------------------------------------
    change=paid-cost

    if change==0:
        print("")
    else:
 #---------------------------------calculates small denominations of change-------------------------------------  
 
        one_d=change//100                   #number of $1 coins
        remainder1=change%100               #remaining change after removing all possible change that could be given using $1 coins
        cent_25=remainder1//25              #number of 25c coins
        remainder2=remainder1%25            #remaining change after removing all possible change that could be given using 25c
        cent_10=remainder2//10              #number of 10c coins
        remainder3=remainder2%10            #remaining change after removing all possible change that could be given using 10c
        cent_5=remainder3//5                #number of 5c coins
        remainder4=remainder3%5             #remaining change after removing all possible change that could be given using 5c
        cent_1=remainder4                   # number of 1c coins

#------------------------------------------Displays Change------------------------------------------------------
    
        print("Your change is:")
        
        if one_d!=0:
            print(one_d,"x","$1")       #displays number of $1 coins
        else:
            print("",end="")
    
        if cent_25!=0:
            print(cent_25,"x","25c")    #displays number of 25c coins
        else:
            print("",end="")
        
        if cent_10!=0:
            print(cent_10,"x","10c")    #displays number of 10c coins
        else:
            print("",end="")
        if cent_5!=0:
            print(cent_5,"x","5c")      #displays number of 5c coins
        else:
            print("",end="")
        if cent_1!=0:
            print(cent_1,"x","1c")      #displays number of 1c coins
        else:
            print("",end="")

    
    
else:
    print("")