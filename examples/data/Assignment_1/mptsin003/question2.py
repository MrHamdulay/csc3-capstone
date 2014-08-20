#Question 2
#Assignment1
#Sinoxolo Mpetsheni

a = eval(input("Enter the hours:\n"))
b = eval(input("Enter the minutes:\n"))
c = eval(input("Enter the seconds:\n"))

if 0<=a<=23:
        
        if 0<=b<=59:
                
                if 0<=c<=59:
                        print("Your time is valid.")
                else:
                        print("Your time is invalid.")
                        
                        
        else:
                print("Your time is invalid.")
                
else:
        print("Your time is invalid.")
        

