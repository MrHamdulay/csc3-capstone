'''program to analyse marks in a file
nicole henning
due 16 may 2014'''

import math

filename = input("Enter the marks filename:\n")

f = open (filename, "r") #opens, read, and closes file = filename
lines = f.readlines ()
f.close ()

for i in range (len (lines)):
    lines[i] = lines[i][:-1] #removing \n from the end of each line

listed = []
for line in lines:
    listed.append(line.split(",")) #create another list by seperating string within existing list


def ave():
    global n #global so that can be used within other functions
    n=0
    summed = 0    
    for i in range(len(listed)):
        n+=1 #counts number of people concerned
    
    for i in range(len(listed)):
        summed+= int(listed[i][1]) #sums total marks of each person concerned
    
    global average  #again global, for future use
    average = summed/n
    print("The average is: {0:0.2f}".format(average)) #gives average, with 2 decimal points


def stand_dev():
    varience = 0
    for i in range(len(listed)):
        varience += ((((int(listed[i][1]) - average))**2)/n) #calculate varience, equal to sum [((x-mean)^2)/n]
    
    global std_dev
    std_dev = math.sqrt(varience) #standard deviation is equal to the sqrt of varience
    print("The std deviation is: {0:0.2f}".format(std_dev)) #formats two decimal places


def names():
    if std_dev > 0:
        print("List of students who need to see an advisor:")    
        for i in range(len(listed)):
            if int(listed[i][1]) < (average - std_dev): #if mark is less than one standard deviation from mean
                print (listed [i][0])
    

ave()
stand_dev()
names()
           