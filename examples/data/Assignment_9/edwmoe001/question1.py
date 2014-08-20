""" Program to calculate if students needs to see advisor
Tauhir egaurdo
5/10/2014"""
import statistics

def failures(number_array,array):
    #check if mark lower than one standard deviation of mean, then add THE POSITION of them to new list 
    #do this so that we can get names of those who need to see advisor via position
    #use statistics module for mean and std.dev - from python 3.4 
    mean = round(statistics.mean(number_array),3)
    strmean = str(mean)
    print("The average is:", "%.2f" % (mean)) # formatting here and 14 for 2 decimal places
    deviation = statistics.pstdev(number_array)
    print("The std deviation is:", "%.2f" % deviation) 
    min_mark = mean - deviation # marks lower than one standard deviation less than mean
    positions = []
    failing = []
    for i in range(len(number_array)): #adds positions of names to list
        if number_array[i] < min_mark:
            positions.append(i)
    for j in range(len(positions)): #adds names to failing list
        k = int(positions[j])
        failing.append(array[k][0])
    return failing
    
    

def main():
    filename = input("Enter the marks filename:\n")
    file = open(filename,"r")
    array = file.readlines ()
    splitarray = []
    for i in range(len(array)):
        line = array[i].split(",")
        splitarray.append(line)
    values = []
    for i in range(len(splitarray)):    # removes "/n" caused from new line text file
        values.append(int(splitarray[i][1]))
        if len(splitarray[i][1]) > 2:
            splitarray[i][1] = splitarray[i][1][:2]
    fail = failures(values,splitarray)
    if fail != []:
        print("List of students who need to see an advisor:")
        for i in range(len(fail)):
            print(fail[i])
main()