# A program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks.

# Categories of marks
first = ""
upper_sec = ""
lower_sec = ""
third = ""
fail = ""


marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(" ")


# Categorizing marks into classes
for i in range (len(marks)):
    if eval(marks[i]) < 50:
        fail += "X"
        
    if 50 <= eval(marks[i]) < 60: 
        third += "X"
        
    if 60 <= eval(marks[i]) < 70:  
        lower_sec += "X"
        
    if 70 <= eval(marks[i]) < 75:  
        upper_sec += "X"
        
    if eval(marks[i]) >= 75: 
        first += "X"
        
        
# Print output as a histogram
print("1 |", first, sep="")
print("2+|", upper_sec, sep="")
print("2-|", lower_sec, sep="")
print("3 |", third, sep="")
print("F |", fail, sep="")
