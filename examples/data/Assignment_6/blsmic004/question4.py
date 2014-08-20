'''program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
Michele Balestra  BLSMIC004
23 April 2014'''

marks = input("Enter a space-separated list of marks:\n")
marks = marks.split()

fail = 0
third = 0
lower = 0
upper = 0
first = 0
for item in marks:
    if eval(item) < 50:
        fail += 1
    if 50 <= eval(item) < 60:
        third += 1
    if 60 <= eval(item) < 70:
        lower += 1
    if 70 <= eval(item) < 75:
        upper += 1
    if 75 <= eval(item) <=100:
        first += 1

print('1 |', 'X' * first, sep='')
print('2+|', 'X' * upper, sep='')
print('2-|', 'X' * lower, sep='')
print('3 |', 'X' * third, sep='')
print('F |', 'X' * fail, sep='')