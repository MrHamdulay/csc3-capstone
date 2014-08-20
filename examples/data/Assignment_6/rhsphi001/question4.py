''' Phillip Ruhesi 
20/04/14
This program checks if a number satisfys the conditions of a category and puts an X in the category'''

x=input('Enter a space-separated list of marks:\n')      #prompts user for input
x=x.split()                                              #split the numbers
#format for the histogram is established
First='1 |'
Upper_second='2+|'
Lower_second='2-|'
Third='3 |'
Fail='F |'
#check if the number satisfys the conditions
for i in x:
    if eval(i)>=75:
        First+='X'
    elif eval(i)>=70:
        Upper_second+='X'
    elif eval(i)>=60:
        Lower_second+='X'
    elif eval(i)>=50:
        Third+='X'
    else:
        Fail+='X'
        
        
print(First)
print(Upper_second)
print(Lower_second)
print(Third)
print(Fail)
 