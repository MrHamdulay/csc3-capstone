#Thembekile Dubazana
#DBZPHI002
#10 March 2014

year= eval(input('Enter a year:\n'))
if ((year%400)/400)==0 :
    print(year,'is a leap year.')
elif ((year%4/4)==0) and ((year%100/100)!=0):
    print(year,'is a leap year.')
else:
    print(year,'is not a leap year.')      