# histogram.py
# a program that takes in a list of marks and outputs a histogram
#   representation of the marks according to the mark categories at UCT.
# Thomas Konigkramer
# 23 April 2014

def marks():
    
    # asks for input from user
    marks = input("Enter a space-separated list of marks:\n")
    
    # input into a list
    list_of_marks = marks.split(" ")
    
    # convert strings in list to numbers
    for i in range(len(list_of_marks)):
        list_of_marks[i] = eval(list_of_marks[i])
    
    # create a dictionary with keys set to different mark classifications
    counter = {"1 ": 0, "2+": 0, "2-": 0, "3 ": 0, "F ": 0}
    
    # enters values in dictionary
    for mark in list_of_marks:
        if mark >= 75:
            counter["1 "] += 1
        elif 70 <= mark < 75:
            counter["2+"] += 1
        elif 60 <= mark < 70:
            counter["2-"] += 1
        elif 50 <= mark < 60:
            counter["3 "] += 1
        elif mark < 50:
            counter["F "] += 1        
    
    # print out output                
    print("1 |", counter["1 "] * "X", sep = "")
    print("2+|", counter["2+"] * "X", sep = "")
    print("2-|", counter["2-"] * "X", sep = "")
    print("3 |", counter["3 "] * "X", sep = "")
    print("F |", counter["F "] * "X", sep = "")


if __name__ == "__main__":
    marks()