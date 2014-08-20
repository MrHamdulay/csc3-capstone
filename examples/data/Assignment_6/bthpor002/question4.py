#A program that takes in  alist of marks and outputs a histogram representation of the marks 
#question 4

#Get the user to input all marks
list_of_marks= input("Enter a space-separated list of marks:\n")

#Make the marks a list by spliting at the spaces 
list_of_marks= list_of_marks.split(" ")

#Separate each of the mark into the different categories
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

#Now to print out the histogram 
print("1 |","X"*len(first),sep="")
print("2+|","X"*len(upper_second),sep="")
print("2-|","X"*len(lower_second),sep="")
print("3 |","X"*len(third),sep="")
print("F |","X"*len(fail), sep="")

      
