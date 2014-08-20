# Determining a leap year
# Monwabisi Dingane
# 7 March 2014


year = int(input("Enter a year:\n"))


outcome = False
    
if year%400==0:
        
        outcome = True
   
elif year%4==0 and year%100!=0:
        
        outcome = True
        
if outcome == True:
                
        print(year,"is a leap year.")
                
else:
                
        print(year,"is not a leap year.")