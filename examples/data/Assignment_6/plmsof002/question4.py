#Grade Histogram
#Sofia Palmer
#23 April 2014

grades = input("Enter a space-separated list of marks:\n")
grades = grades.split(" ")

#define variables
count1 = 0
count2u = 0
count2l = 0
count3 = 0
countF = 0

#check every grade and count how many go into each category 
for i in range(len(grades)):
    grade = eval(grades[i])
    if grade >= 75:
        count1 +=1
    elif grade >= 70:
        count2u +=1
    elif grade >= 60:
        count2l +=1
    elif grade >= 50:
        count3 += 1
    else:
        countF += 1

#print histogram
print("1 |",count1*"X", sep = '')
print("2+|",count2u*"X", sep = '')
print("2-|",count2l*"X", sep = '')
print("3 |",count3*"X", sep = '')
print("F |",countF*"X", sep = '')
