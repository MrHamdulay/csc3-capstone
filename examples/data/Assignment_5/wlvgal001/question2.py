#Question2 change 
#Galya Wolov
#14 April 2014

#state all variables used throughout function:
amount= 0
itemprice = eval(input("Enter the cost (in cents):\n")) #getting price of item from user
dol= ((amount - itemprice)//100)
twentyfive = ((amount - itemprice - dol)/25)  
tenc= (amount - itemprice - dol-twentyfive)/10
fivec= (amount- itemprice- dol- twentyfive- tenc)/5
onec=(amount- itemprice- dol- twentyfive- tenc-fivec)/1

#get amount of change from user        
amount = 0

while itemprice >amount:
        amount +=eval(input("Deposit a coin or note (in cents):\n"))
        

#return change to user in relevant coins
while amount - itemprice> 0:
        print("Your change is:")
        if 0< (amount-itemprice):
                dol =((amount - itemprice)//100)
                if dol>0:
                        print ( dol, "x $1")
                if (amount- itemprice- dol*100) ==0 :
                        break
                #the above if statement recurs throughout the program to end if the amount owed becomes zero to prevent the infinite loop from iterating infintitely.
                        

        if  (amount - itemprice - dol) >0:
                twentyfive = (amount - itemprice - dol*100)//25
                if twentyfive>0:                
                        print (twentyfive, "x 25c")
                if (amount- itemprice- dol*100-twentyfive*25) ==0 :
                        break                
                        
        
                if (amount - itemprice - dol*100-twentyfive*25)/10 >0:
                        tenc= (amount - itemprice - dol*100-twentyfive*25)//10
                        if tenc>0:
                                print(tenc, "x 10c")
                        if (amount- itemprice- dol*100-twentyfive*25-tenc*10) ==0 :
                                break                        
                                
                        
                        if (amount - itemprice - dol*100- twentyfive*25 - tenc*10) > 0:
                                fivec= (amount- itemprice- dol*100- twentyfive*25 -tenc*10) // 5
                                if fivec>0:
                                        print (fivec, "x 5c")
                                if (amount- itemprice- dol*100-twentyfive*25-tenc*10-fivec*5) ==0 :
                                        break                                
                                        

                                if (amount - itemprice - dol*100- twentyfive*25 - tenc*10-fivec*5)>0 :
                                        onec=(amount- itemprice- dol*100- twentyfive*25- tenc*10-fivec*5)//1
                                        if onec>0:
                                                print (onec, "x 1c")
                                                break