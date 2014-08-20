"""Lenard Carroll
24 April 2014
Assignment 6"""

mark = input("Enter a space-separated list of marks:\n") # User is prompted to type in a few numbers/marks
marks = mark.split() # The numbers are then split

counters = {}

for mark in marks:
    if not mark in counters:
        counters[mark] = 0 
    counters[mark] += 1 #This counts the occurences of each number in the list
    
x = eval(mark)
x_50 = 0
x_60 = 0
x_70 = 0
x_75 = 0
x_100 = 0

sorted_marks = sorted(counters.keys())

# This part down here will determine the number of occurences of the numbers in a certain range
for mark in sorted_marks:
    if x>=0 and x<50:
        x_50 += counters[mark]
        
for mark in sorted_marks:
    if x>=50 and x<60:
        x_60 += counters[mark]
        
for mark in sorted_marks:
    if x>=60 and x<70:
        x_70 += counters[mark]
        
for mark in sorted_marks:
    if x>=70 and x<75:
        x_75 += counters[mark]
        
for mark in sorted_marks:
    if x>=75 and x<100:
        x_100 += counters[mark]

print('1 |'+'X'*x_100)
print('2+|'+'X'*x_75)
print('2-|'+'X'*x_70)
print('3 |'+'X'*x_60)
print('F |'+'X'*x_50)
    