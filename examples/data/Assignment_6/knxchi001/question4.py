#Assignment 6
#question 4

#Get user to input all marks
list_of_marks= input("Enter a space-separated list of marks:\n")

#Seperate marks into list
list_of_marks= list_of_marks.split(" ")

#Split marks into categories
fail=[]
third=[]
lower_second=[]
upper_second=[]
first=[]
for mark in list_of_marks:
    if eval(mark) < 50:
        fail.append(mark)
    elif 50 <= eval(mark) < 60:
        third.append(mark)
    elif 60<= eval(mark) < 70:
        lower_second.append(mark)
    elif 70 <= eval(mark) < 75:
        upper_second.append(mark)
    else:
        first.append(mark)

#Print out Histogram
print("1 |","X"*len(first),sep="")
print("2+|","X"*len(upper_second),sep="")
print("2-|","X"*len(lower_second),sep="")
print("3 |","X"*len(third),sep="")
print("F |","X"*len(fail), sep="")

      
