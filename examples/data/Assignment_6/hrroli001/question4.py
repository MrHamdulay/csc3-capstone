# Question 3 - Assignment 6
# Oliver Harrison
# 21 April 2014

# Get Marks

marks_string=(input("Enter a space-separated list of marks:\n"))

marks = marks_string.split(" ")

# Count 
fail=0
three=0
two_minus=0
two_plus=0
one=0

for i in marks:
    i=eval(i)
    if i<50:
        fail += 1
    elif 50<=i<60:
        three += 1
    elif 60<=i<70:
        two_minus += 1
    elif 70<=i<75:
        two_plus += 1
    else:
        one += 1

print("1 |", "X"*one, sep="")
print("2+|", "X"*two_plus, sep="")
print("2-|", "X"*two_minus, sep="")
print("3 |", "X"*three, sep="")
print("F |", "X"*fail, sep="")
    
# Print