"""program that takes in a list of marks and converts them to a histogram
Jacqueline Blomendahl
23/04/2014"""

#getting input
marks= input("Enter a space-separated list of marks:\n")
sep_marks = marks.split()

#creating counters
fail_counter=0
counter_3=0
counter_2_lower=0
counter_2_upper=0
counter_1st=0

#decision tree to categorize
for i in sep_marks:
    i=eval(i)
    if (i < 50):
        fail_counter+=1
    elif i >= 50 and i < 60:
        counter_3+=1
    elif i >= 60 and i < 70:
        counter_2_lower+=1
    elif i >= 70 and i < 75:
        counter_2_upper+=1
    elif i >= 75:
        counter_1st+=1

#print output
print("1 |", counter_1st*"X", sep='')
print("2+|", counter_2_upper*"X", sep='')
print("2-|", counter_2_lower*"X", sep='')
print("3 |", counter_3*"X", sep='')
print("F |", fail_counter*"X",sep='')