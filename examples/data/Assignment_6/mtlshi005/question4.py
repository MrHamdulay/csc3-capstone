#Shivaan Motilal
#22/04/14

#user enters string of marks, convert to list
print("Enter a space-separated list of marks:")

listm=input()
listm=listm.split(" ")




#categorizing marks 
fail=0
third=0
lower_2nd=0
upper_2nd=0
first=0

for num in listm:
    num=eval(num)
    if num<50:
        fail+=1
    
    elif num>=50 and num<60:
        third+=1
        
    elif num>=60 and num<70:
        lower_2nd+=1
        
    elif num>=70 and num<75:
        upper_2nd+=1
        
    else:
        first+=1
#print out histogram
print("1 |",first*"X",sep="")
print("2+|",upper_2nd*"X",sep="")
print("2-|",lower_2nd*"X",sep="")
print("3 |",third*"X",sep="")
print("F |",fail*"X",sep="")
