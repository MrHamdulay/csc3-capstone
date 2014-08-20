'''find average and std dev in students marks
nic findlay
15 may 2014'''
import math

def marks(): 
    file_name = input("Enter the marks filename:\n")
    infile = open(file_name,"r")
    text_list = infile.readlines()
    #print(text_list)
    new_list = []
    for i in range(len(text_list)):
        new_list.append(text_list[i].split(",")) #create list from input file text
    
    for i in range(len(new_list)):
        new_list[i][1] = eval(new_list[i][1]) 
    
    infile.close()
    return text_list, new_list


def mean(new_list): 
    total = 0
    entries = len(new_list)
    for i in range(len(new_list)):
        total += new_list[i][1]
    average = total / entries
    
    return average


def std_dev(average,new_list): #calculate the standard deviation 
    sum_variance = 0
    for i in range(len(new_list)):
        sum_variance += (new_list[i][1]-average)**2    
    deviation = math.sqrt(sum_variance / len(new_list))
    return deviation

def fail(new_list,standard_deviation,average): #students who are below 1 std_dev
    low_students = []
    required = average - standard_deviation
    for i in range(len(new_list)):
        if new_list[i][1] < required:
            low_students.append(new_list[i][0])
    return low_students    

def main():
    text_list,new_list = marks()
    average = mean(new_list)
    print("The average is:","{:.2f}".format(average))
    dev = std_dev(average,new_list)
    print("The std deviation is:","{:.2f}".format(dev))
    low_students = fail(new_list,dev,average)
    if len(low_students) > 0:
        print("List of students who need to see an advisor:")
        for i in range(len(low_students)):
            print(low_students[i])
main()
