#a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
#get input from user 
x=input('Enter a space-separated list of marks:\n')
#initialise counters for the different categories 
first=0
upper_second=0
lower_second=0
third=0
fail=0
#create an empty list
marks=[]
#loop over the split inputs, convert to a number and add to list 
for num in x.split():
    num=int(num)
    marks.append(num)
#loop over the individual marks and categorise according to being greater than or less than a particular parameter   
for i in range(len(marks)):
    
    if marks[i]>=75:
        first+=1
    elif 70 <= marks [i]<75:
        upper_second+=1
    elif 60 <= marks [i]<70:
        lower_second+=1
    elif 50 <= marks [i]<60:
        third+=1
        
    else:
        if marks[i]<50:
            fail+=1
#print output in the form of a histogram            
print('1 |'+'X'*first)
print('2+|'+'X'*upper_second)
print('2-|'+'X'*lower_second)
print('3 |'+'X'*third)
print('F |'+'X'*fail)
        
        