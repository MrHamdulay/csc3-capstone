#Dudley program to calculate leap year
#written 12/3/14

def leapye():
    input2=eval(input("Enter a year:\n"))
    a=input2%400
    
    if a == 0: 
        print (input2,"is a leap year.")
    else:

        b=input2%4
        c=input2%100
        if (b== 0 and c!=0):
            print (input2,"is a leap year.")
       
        else:
            print(input2,"is not a leap year.")
            
leapye()
        
    

           