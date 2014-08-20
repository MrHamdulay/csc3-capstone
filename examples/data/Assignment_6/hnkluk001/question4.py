# Luke Henkeman
# HNKLUK001
# 25 April 2014
# question4.py
# create a histogram of class marks

def markhist():
    marklist = input("Enter a space-separated list of marks:\n")
    marks = marklist.split(" ")
#    print(marks)
    fail = []
    third = []
    lower2 = []
    upper2 = []
    first = []
    nummarks = len(marks)
    for i in range(nummarks):
        if int(marks[i]) >= 75:
            first.append(marks[i])
        elif int(marks[i]) >= 70:
            upper2.append(marks[i])
        elif int(marks[i]) >= 60:
            lower2.append(marks[i])
        elif int(marks[i]) >= 50:
            third.append(marks[i])
        else:
            fail.append(marks[i])
    print("1 |",len(first)*"X",sep="")
    print("2+|",len(upper2)*"X",sep="")
    print("2-|",len(lower2)*"X",sep="")
    print("3 |",len(third)*"X",sep="")
    print("F |",len(fail)*"X",sep="")
    
markhist()