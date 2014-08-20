#A program that draws a histogram of marks according to UCT mark categories
#Megan Swartz
#24 April 2014

def marks():
    
    #get a space-separated list of marks
    marks = input("Enter a space-separated list of marks:\n")
    marks = marks.split(" ")
    
    #an array for counters for each category
    count_first = []
    count_uppersecond = []
    count_lowersecond = []
    count_third = []
    count_fail = []
    
    #find the number of marks in each category
    for i in marks:
        if int(i) >= 75:
            count_first.append("X")
        elif int(i) >= 70:
            count_uppersecond.append("X")
        elif int(i) >= 60:
            count_lowersecond.append("X")
        elif int(i) >= 50:
            count_third.append("X")
        else:
            count_fail.append("X")
    
    #print out histogram
    print("1 |", "".join(count_first), sep = "")
    print("2+|", "".join(count_uppersecond), sep = "")
    print("2-|", "".join(count_lowersecond), sep = "")
    print("3 |", "".join(count_third), sep = "")
    print("F |", "".join(count_fail), sep = "")

marks()