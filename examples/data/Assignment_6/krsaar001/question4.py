# Aaron Krishna
# 24 April 2014
# A program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT

first = 0 #stores the number of 1st
upper_second = 0 #stores the number of 2+
lower_second = 0 #stores the number of 2-
third = 0 #stores the number of 3rd
fail = 0 #stores the number of fails
marks = input("Enter a space-separated list of marks:\n") #requests user to enter marks
marks = marks.split(" ") #splits marks by spaces - creates a string array of marks

for position in range(len(marks)): #I think this is pretty self-explanatory
    if eval(marks[position]) >= 75: 
        first += 1
    elif 70 <= eval(marks[position]) < 75:
        upper_second += 1
    elif 60 <= eval(marks[position]) < 70:
        lower_second += 1
    elif 50 <= eval(marks[position]) < 60:
        third += 1
    elif eval(marks[position]) < 50:
        fail += 1
        
print("1 |" + ("X" * first)) #And these are just the output in the form of a histogram
print("2+|" + ("X" * upper_second))
print("2-|" + ("X" * lower_second))
print("3 |" + ("X" * third))
print("F |" + ("X" * fail))