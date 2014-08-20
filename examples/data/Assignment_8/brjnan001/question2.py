"""Assignment 8-Q2
Nandani Birjanund
4 May 2014"""

input_by_user=input("Enter a message:\n") #user inputs a string

def Pairs(input_by_user):
   
    if input_by_user=="": #user inputs an empty string
        return 0 #nothing
    elif(len(input_by_user)==1): #length of 1 in string
        return 0 #nothing
   
    else:
       
        if input_by_user[0]==input_by_user[1]: #first letter of input= second letter
            input_by_user=input_by_user[2:] 
            return 1+Pairs(input_by_user) 
        else:
            return Pairs(input_by_user[1:]) 
       
function=Pairs(input_by_user)
print("Number of pairs: " +str(function)) #Number of pairs with str function