"""program to read marks from a file and determine who needs assistance
Tim Hardie
16 May 2014"""

import math

#function to calculate the mean mark of a list
def calc_mean (mark_list):
    mean_mark = 0
    for i in range (len (mark_list)):
        mean_mark += eval (mark_list[i][1])
    mean_mark /= len (mark_list)
    return mean_mark
    
#function to calculate standard deviation of a list of marks
def calc_stddev (mark_list, mean):
    std_dev = 0
    for i in range (len (mark_list)):
        std_dev += (eval (mark_list[i][1]) - mean)**2
    std_dev = (std_dev / len (mark_list))**0.5
    return std_dev

if __name__ == "__main__":
    #get values from file
    filename = input ("Enter the marks filename:\n")
    f = open (filename, 'r')
    mark_list = f.readlines ()
    f.close ()
    
    #remove new line character & split marks and names
    for i in range (len (mark_list) -1):
        mark_list[i] = mark_list[i][:-1].split (',')
    mark_list[len (mark_list)-1] = mark_list[len (mark_list)-1].split (',')
    
    #get values for mean and std deviation
    mean = calc_mean (mark_list)
    print ("The average is: {:.2f}".format (mean))
    std_dev = calc_stddev (mark_list, mean)
    print ("The std deviation is: {:.2f}".format (std_dev))
    
    help_list = []
    for i in range (len (mark_list)):
        if (eval (mark_list[i][1]) < mean - std_dev):
            help_list.append (mark_list[i][0])
    if help_list:
        print ("List of students who need to see an advisor:")
        for name in help_list:
            print (name)