# James Behr
# 2014-04-23
# Assignment 6 Question 4

def printlabel(label, count):
    '''Print out a histogram 'label' and a 'count' number of Xs'''
    print('{:2}|{}'.format(label, 'X' * count))
  
def rangefilter(lst, lower, upper):
    '''Return 'lst' where the values lie between upper and lower'''
    return [item for item in lst if lower <= item < upper]
    
print('Enter a space-separated list of marks:')
inputstr = input()
# Split list and convert each item to integer using list comprehension
marks = [int(item) for item in inputstr.split()]

printlabel('1', len(rangefilter(marks, 75, 101)))
printlabel('2+', len(rangefilter(marks, 70, 75)))
printlabel('2-', len(rangefilter(marks, 60, 70)))
printlabel('3', len(rangefilter(marks, 50, 60)))
printlabel('F', len(rangefilter(marks, 0, 50)))