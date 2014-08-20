__author__ = 'George de Kock'
"""Histogram representation of the marks according to the mark categories at UCT
    2014-4-20   """
marks = input("Enter a space-separated list of marks:\n").split(" ")
counter = [0,0,0,0,0]
symbols = ["1 ","2+","2-","3 ","F "]

for mark in marks:
    mark = eval(mark)
    if mark >= 75:
        counter[0] += 1
    elif mark >= 70:
        counter[1] += 1
    elif mark >= 60:
        counter[2] += 1
    elif mark >= 50:
        counter[3] += 1
    else:
        counter[4] += 1

for i in range(len(counter)):
    print(symbols[i],"|","X"*counter[i],sep="")