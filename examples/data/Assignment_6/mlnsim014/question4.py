'''program to represents marks according to mark categories
question4, assignment6
Simangaliso Mlangeni
MLNSIM014
24 April 2014'''

#create function to calculate to represent marks
def marksRepresentation() :
#prompt user to enter space-separated marks
    marksList = input("Enter a space-separated list of marks:\n")
    marksList = marksList.split(" ")#converts string into list
#create empty list to append marks to regarding each category
    first = []
    upper2nd = []
    lower2nd = []
    third = []
    fail = []
#loop that iterates through each mark in the list and appends marks falling under each category 
    for i in marksList:
        mark = eval(i)
        if 0<= mark < 50:
            fail.append(mark)
        elif 50 <= mark < 60:
            third.append(mark)
        elif 60 <= mark < 70:
            lower2nd.append(mark)
        elif 70 <= mark < 75:
            upper2nd.append(mark)
        elif 75 <= mark <= 100:
            first.append(mark)
#prints out histogram representing marks and number of people who obtained those marks in each category             
    print("1 |","X"*(len(first)),sep="")
    print("2+|","X"*(len(upper2nd)),sep="")
    print("2-|","X"*(len(lower2nd)),sep="")
    print("3 |","X"*(len(third)),sep="")
    print("F |","X"*(len(fail)),sep="")

marksRepresentation()