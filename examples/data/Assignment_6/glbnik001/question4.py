def grader():
    MarkList = []
    import math
    # This line splits the input and creates the mark list
    grades = input("Enter a space-separated list of marks:\n")
    i = 0
    for i in grades.split():
        if i == " ":
            jinx = 0 #programme should do nothing if i = " "
        elif i != " ":
            i = int(i)
            MarkList.append(i)
        i = 0
    # This next line is designed to iterate through the marke list and sort the grades into their respective categories
    first = 0
    usecond = 0
    lsecond = 0
    third = 0
    fail = 0
    for x in MarkList:
        if x >= 75:
            first += 1
        elif 75 > x >= 70:
            usecond += 1
        elif 70 > x >= 60:
            lsecond += 1
        elif 60 > x >= 50:
            third += 1
        elif x <= 50:
            fail += 1
    print ("1 |","X"*first,sep="")
    print ("2+|","X"*usecond,sep="")
    print ("2-|","X"*lsecond,sep="")
    print ("3 |","X"*third,sep="")
    print ("F |","X"*fail,sep="")
grader()