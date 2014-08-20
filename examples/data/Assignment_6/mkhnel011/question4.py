""" a program that takes a list of marks and prints out a histogram of them according to category
nelisile mkhwebane
23/04/2014"""

""" get the marks from the user"""

marks = input ("Enter a space-separated list of marks:\n")

"""split the list of marks"""
marks_str=marks.split(" ")

""" the categories """
fail = []
third = []
lowersec = []
uppersec = []
first = []

""" initialising the counts of each category """

count_fail = 0
count_third = 0
count_lowersec = 0
count_uppersec = 0
count_first = 0

""" finding out what category the marks lie"""

for i in marks_str:
    if eval(i) < 50:
        fail.append(i)
        count_fail+=1
    elif eval(i) >= 50 and eval(i)< 60:
        third.append(i)
        count_third+=1
    elif eval(i) >= 60 and eval(i)<70:
        lowersec.append(i)
        count_lowersec+= 1
    elif eval(i) >= 70 and eval(i) <75:
        uppersec.append(i)
        count_uppersec+=1
    else:
        first.append(i)
        count_first+=1
""" printing out the histogram"""

print("1 |","X"*count_first, sep="")
print("2+|","X"*count_uppersec,sep="")
print("2-|","X"*count_lowersec,sep="")
print("3 |","X"*count_third,sep="")
print("F |","X"*count_fail,sep="")
