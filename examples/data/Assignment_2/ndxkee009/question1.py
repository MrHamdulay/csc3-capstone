#Keegan Naidoo
#NDXKEE009

y=eval(input(("Enter a year: \n")))

if(y%400==0):
    
    print(y," is a leap year.",sep='')
    
elif(y%100==0):
    
    print(y," is not a leap year.",sep='')
        
elif(y%4==0):
    
    print(y," is a leap year.",sep='')
    
else:
    
    print(y," is not a leap year.",sep='')