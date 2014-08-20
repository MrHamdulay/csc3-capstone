'''Histogram representing marks
Michael Sanne
2014/04/20'''

#Accepts list of marks and stores it in a list
marks_str = input("Enter a space-separated list of marks:\n")
marks = (marks_str.split (" "))

one = 0
twoUpper = 0
twoLower = 0
three = 0
fail = 0
#Counts the occurences of a 1st, upper 2nd lower 2nd, 3rd and a fail
for i in range (len (marks)):
    if (eval(marks[i]) < 50):
        fail += 1
    if (50 <= eval(marks[i]) < 60):
        three += 1
    if (60 <= eval(marks[i]) < 70):
        twoLower += 1
    if (70 <= eval(marks[i]) < 75):
        twoUpper += 1
    if (eval(marks[i]) >= 75):
        one += 1
#Prints the results where 'X' represents one occurence      
print ("1 |" +(one*"X"))
print ("2+|" +(twoUpper*"X"))
print ("2-|" +(twoLower*"X"))
print ("3 |" +(three*"X"))
print ("F |" +(fail*"X"))