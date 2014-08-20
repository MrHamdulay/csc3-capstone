"""Program to create textfile and use it to calculate stuff
Khanyisile Morudu
11 May 2014 """

#variables
marks = 0
adv_list = ""
avg = 0
std = 0
counter = 0
a = "{0:.2f}"

# get the first input
#student = input ("")
    
#doing the calculations
filename = input("Enter the marks filename:\n")

f = open(filename, "r")
#getting average 
for line in f:
    pos = line.index(",")
    marks = marks + int(line[pos + 1: len(line)])
    counter = counter + 1
f.close()
#avg
avg = marks/counter

#standard deviation
f = open(filename, "r")
for line in f:
    pos = line.index(",")
    mark = int(line[pos + 1: len(line)])
    std = std + (mark - avg)**2
    
f.close()

std = (std /counter)**0.5

#getting list for advisor
one_std = avg - std
f = open(filename, "r")
for line in f:
    pos = line.index(",")
    mark = int(line[pos + 1: len(line)])
    if mark < one_std:
        adv_list = adv_list + line[:pos] + "\n"   
f.close

print("The average is:", a.format(avg))
print("The std deviation is:", a.format(std))
if adv_list != "":
    print("List of students who need to see an advisor:")
    print(adv_list)

