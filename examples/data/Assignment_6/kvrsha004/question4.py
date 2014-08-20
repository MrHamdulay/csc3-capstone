""" Q4 of Assignment 6: Histogram
 KVRSHA004
 20th April 2014 """

marks = input("Enter a space-separated list of marks: \n")
marklist = marks.split(" ") #array of marks
counter = [0, 0, 0, 0, 0] #F, 3rd, lower2nd, upper2nd, 1st

for i in marklist: #evaluate each mark; add 1 to respective counter
    if eval(i)<50:
        counter[0] += 1
    elif 50<=eval(i)<60:
        counter[1] += 1
    elif 60<=eval(i)<70:
        counter[2] += 1
    elif 70<=eval(i)<75:
        counter[3] += 1
    elif eval(i)>=75:
        counter[4] += 1    

#histogram with X times number of marks in each class 
print("1 |"+(counter[4]*"X"))
print("2+|"+(counter[3]*"X"))
print("2-|"+(counter[2]*"X"))
print("3 |"+(counter[1]*"X"))
print("F |"+(counter[0]*"X"))