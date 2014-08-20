# program that takes in a list of marks and outputs a histogram
# mllgad001
# 24 April 2014
    
marks = input("Enter a space-separated list of marks: \n") # prompts user to enter list of marks
marks = marks.split(' ')
list_ = [] # empty list to store marks
    
for i in marks:
    list_.append(eval(i)) # converts each separate string to an integer and adds it to empty list
first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0

for mark in list_: # loops through every number in the list 
    # determine under which category the mark falls, and add 1 to that category
    if mark >= 75 :
        first += 1
    if 75 > mark >= 70 :
        upper_second += 1
    if 70 > mark >= 60 :
        lower_second += 1
    if 60 > mark >= 50 :
        third += 1
    if mark < 50 :
        fail += 1
        
# print the histogram representation         
print("1 ", "|", "X"*first, sep="")
print("2+", "|", "X"*upper_second, sep="")
print("2-", "|", "X"*lower_second, sep="")
print("3 ", "|", "X"*third, sep="")
print("F ", "|", "X"*fail, sep="")   
