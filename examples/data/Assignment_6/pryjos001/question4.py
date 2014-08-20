"""program to output histogram representation of marks
Joseph Preyer
24 April 2014"""

marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(" ")

#convert values to integers
for i in  range(len(marks)):
    marks[i] = eval(marks[i])

#create dictionary for categories
marks_count={"F":0, "3":0, "2-":0, "2+":0, "1":0}
for i in marks:
    if i<50:
        marks_count["F"]+=1
    elif 50<=i<60:
        marks_count["3"]+=1
    elif 60<=i<70:
        marks_count["2-"]+=1
    elif 70<=i<75:
        marks_count["2+"]+=1
    else:
        marks_count["1"]+=1

print ("1 |", marks_count["1"]*"X", sep="")
print ("2+|", marks_count["2+"]*"X", sep="")
print ("2-|", marks_count["2-"]*"X", sep="")
print ("3 |", marks_count["3"]*"X", sep="")
print ("F |", marks_count["F"]*"X", sep="")