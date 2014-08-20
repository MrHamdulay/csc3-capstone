#Leap year program
#Nic Findlay

def leap(number):
        if number%400==0: #% gives remainder, so when it is equal to 0 then there is no remainder
                print(number,"is a leap year.")
        else: 
                if (number%4==0) and (number%100==0):
                        print(number,"is not a leap year.")
                else:
                        if number%4==0:
                                print(number,"is a leap year.")
                        else:
                                if number%100==0:
                                        print(number,"is a leap year.")
                                else: print(number,"is not a leap year.")
                                
x=eval(input("Enter a year:\n"))
leap(x)
             
    
    
