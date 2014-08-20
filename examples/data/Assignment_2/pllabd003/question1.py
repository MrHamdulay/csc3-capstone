# Abdul-Azeez Pillay
# 10/3/2014
# Assignmnet 2 question 1

x= eval(input("Enter a year:\n"))
if(x%4==0 and (x/4)%100>=0 and (x/4)%100<5):
    print(x, "is a leap year.")
    
else: print(x, "is not a leap year.")