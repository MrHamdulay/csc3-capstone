#jono field
#24 April
#Question 4

Marks=input("Enter a space-separated list of marks:\n") #asks user to input marks
list=Marks.split() #splits list of marks
list=map(int,list) #converts strings to integers


fail, third, lower2nd, upper2nd, first = 0,0,0,0,0 #set counts to 0 

for Marks in list: #loop created
    
    if 0<=Marks<50: #if mark between 0 and 50 then add to fail
        fail = fail + 1
    elif 50<=Marks<60: #if mark between 50 and 60 then add to third
        third = third + 1
    elif 60<=Marks<70: #if mark between 60 and 70 then add to lower 2nd
        lower2nd = lower2nd + 1
    elif 70<=Marks<75: #if mark between 70 and 75 then add to upper 2nd
        upper2nd = upper2nd + 1
    elif 75<=Marks<=100: #if mark between 75 and 100 then add to 1st
        first = first + 1
    else:
        None
        
        
print("1 |", "X"*first, sep="")    #histogram is created
print("2+|", "X"*upper2nd, sep="")
print("2-|", "X"*lower2nd, sep="")
print("3 |", "X"*third, sep="")
print("F |", "X"*fail, sep="")


        
        
             
        
        
