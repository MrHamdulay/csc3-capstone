#vrmnic005
#assignment 9, question 1

from math import sqrt

marks = {}
names_list = []

file = input("Enter the marks filename:\n")

with open(file,"r") as data:
    for line in data:
        name, mark = line.split(",")
        mark = int(mark)
        names_list.append(name)
        marks[name] = mark

average = sum(marks.values()) / len(marks)

standard_dev = sqrt(sum([(x - average)**2 for x in marks.values()]) / len(marks))

print("The average is: {:.2f}".format(average))
print("The std deviation is: {:.2f}".format(standard_dev))

header_printed = False
for name in names_list:
    if marks[name] < average - standard_dev:
        if not header_printed:
            print("List of students who need to see an advisor:")
            header_printed = True
        print(name)
