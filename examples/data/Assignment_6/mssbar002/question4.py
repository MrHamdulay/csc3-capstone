"""a program that takes in a list of marks (separated by spaces) 
and outputs a histogram representation of the marks according to the 
mark categories at UCT
Author: Barnett Msiska
Date: 23/04/2014"""

def main():
    one = 0
    twoPlus = 0
    twoMinus = 0
    three = 0
    fail = 0
    marksString = input("Enter a space-separated list of marks:\n")
    marks = marksString.split(" ")
    intMarks = []
    for m in marks:
        intMarks.append(int(m))
    for m in intMarks:
        if m >= 75:
            one += 1
        elif 70 <= m < 75:
            twoPlus += 1
        elif 60 <= m < 70:
            twoMinus += 1
        elif 50 <= m < 60:
            three += 1
        else:
            fail += 1 
    print("1 |" + "X"*one)
    print("2+|" + "X"*twoPlus)
    print("2-|" + "X"*twoMinus)
    print("3 |" + "X"*three)
    print("F |" + "X"*fail)
                
main()