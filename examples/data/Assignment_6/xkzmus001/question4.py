"""question4.py
Auhtor : Musa Xakaza
Date : 19/04/2014"""

#get numbers as a string, split them into a list
marks= input("Enter a space-separated list of marks:\n").split(' ')
first, upper2nd, lower2nd, third, fail = 0, 0, 0, 0, 0

for mark in marks:
    #convert mark, which was stored as a string, to an integer 
    mark = int(mark)
    if 0 <= mark < 50 : fail += 1
    elif 50 <= mark < 60 : third += 1
    elif 60 <= mark < 70 : lower2nd += 1
    elif 70 <= mark < 75 :upper2nd += 1
    elif 75 <= mark < 101 : first += 1
    
print("1 |", 'X'*first, sep='')
print("2+|", 'X'*upper2nd, sep='')
print("2-|", 'X'*lower2nd, sep='')
print("3 |", 'X'*third, sep='')
print("F |", 'X'*fail, sep='')