#Shaylan Lalloo
#15/05/2014
#Find standard deviation, average of marks as well as those names below one std of the avg


from math import *

fname = input('Enter the marks filename:\n')
#get file name
f = open(fname, 'r')
#open file to read
names = f.readlines()
#read names in
f.close()

for i in range(len(names)):
    names[i] = names[i][:-1]
    names[i] = names[i].split(',')
    names[i][1] = int(names[i][1])
#drops new line character. Splits the string into name and mark and makes mark an integer

mean = 0
for i in names:
    mean += i[1]
#finds sum

mean /= len(names)
#turns sum into mean

print('The average is:', '{0:.2f}'.format(round(mean, 2)))
#output formatted mean

sd = 0
#sets standard deviation

for i in range(len(names)):
    sd += (mean - names[i][1]) ** 2
#increase by squares

sd /= len(names)
#divides by number of students
sd = sqrt(sd)
#then squareroots answer

print('The std deviation is:', '{0:.2f}'.format(round(sd, 2)))
#output std deviation

mycount = 0

for i in range(len(names)):
    #checks if below one sd of the mean
    if names[i][1] < mean - sd:
        if mycount == 0:
            print('List of students who need to see an advisor:')
            #check if first name to output then prints heading
        mycount += 1
        print(names[i][0])
        #outputs name

