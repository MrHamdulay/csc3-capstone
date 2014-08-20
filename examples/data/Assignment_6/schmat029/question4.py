#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     sorting marks into categories
#
# Author:      Matthias
#
# Created:     22-04-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

marks = input("Enter a space-separated list of marks: \n")
marks = marks.split()
categories = [["1",0],["2+",0],["2-",0],["3",0],["F",0]]

# sort marks into categories
for i in marks:
    if eval(i) >= 75:
        categories[0][1] += 1
    elif eval(i) >= 70:
        categories[1][1] += 1
    elif eval(i) >= 60:
        categories[2][1] += 1
    elif eval(i) >= 50:
        categories[3][1] += 1
    else:
        categories[4][1] += 1

# print out categories with axes and labels
i = 0
while i < len(categories):
    print("{0:<2}|".format(categories[i][0]) + "X"*categories[i][1])
    i += 1