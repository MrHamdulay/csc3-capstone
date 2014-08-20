"""Assignment 6
question 4
Mphuhti Mamorena
21 April 2014"""


marklist=input('Enter a space-separated list of marks:\n')
list=marklist.split(' ') # making a list
# initalising the catagories
F=0
third=0
low2cnd=0
up2cnd=0
first=0
# counting the number of marks that satisfy the conditions for each category
for i in list:
    i=int(i)
    if i<50 and i>=0:
        F+=1
    elif i>=50 and i<60:
        third+=1
    elif i>=60 and i<70:
        low2cnd+=1
    elif i>=70 and i<75:
        up2cnd+=1
    elif i>=75 and i<=100:
        first+=1
    else:
        print("mark out of range")
     
print('1','|'+'X'*first)
print('2+'+'|'+'X'*up2cnd)
print('2-'+'|'+'X'*low2cnd)
print('3','|'+'X'*third)
print('F','|'+'X'*F)

    
    