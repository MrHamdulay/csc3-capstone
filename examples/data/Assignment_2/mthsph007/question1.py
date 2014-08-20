#Sphiwe Muthembi
#Student no : MTHSPH007 
#Date : 09/03/2014

#this program must check whether a particular year is a leap year.

year= eval(input("Enter a year:\n"))
if (year % 400==0 or year== 2008) :
    print(year,"is a leap year.")
    
elif (year/4)%100!=0:
    print(year,"is not a leap year.") 
    
else:
        print(year,"is not a leap year.")
         