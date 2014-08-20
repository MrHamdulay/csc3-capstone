#SNGSOH004
#Assignment 6
#Question 1
#23rd April 2014

marks = map(int, input("Enter a space-separated list of marks:\n").split(" ")) #creating a matrix of the marks
counter = [0] * 5

for i in marks: #allocating the mark to a grade category
    if i>=75:
        k=0
    elif i>=70:
        k=1
    elif i>=60:
        k=2
    elif i>=50:
        k=3
    else:
        k=4
    counter[k]+=1 
    
levels = ["1 ", "2+", "2-", "3 ", "F "] #the different grading categories
for l in range(len(counter)):
    print(levels[l] + "|" + "X" * counter[l])