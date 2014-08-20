""" Skhulile Thenjwayo
Assignment 9 question1
12/05/2014"""

filename=input("Enter the marks filename:\n")
f = open(filename,"r")
lines = f.readlines()
f.close()
summ =0
part = []
for i in range(len(lines)):
    #to calculate sum of all marks
    part = lines[i].split(",")
    part[1] = part[1][:-1]
    summ+=eval(part[1])
average = summ/len(lines)
print("The average is: {0:5.2f}".format(average))
varien = 0
for i in range(len(lines)):
    #calculates varience
    part = lines[i].split(",")
    varien += (eval(part[1])-average)**2
stdev = (varien/len(lines))**.5
print("The std deviation is: {0:5.2f}".format(stdev))
print("List of students who need to see an advisor:")
for i in range(len(lines)):
    #determines which students are more than a standard deviations from the mean
    part = lines[i].split(",")
    if eval(part[1])<= (average-stdev) :
        print(part[0])