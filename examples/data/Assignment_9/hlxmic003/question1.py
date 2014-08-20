# Michaela Heale
# Assignment 9 Question 1
#Student Marks

import math 
def main():
    marks = []
    #reads in textfile name
    name = input("Enter the marks filename:\n")
    try: #exception handling
        file = open(name,'r')
        count = 0
        cc = count_lines(name)
        #creates an array of names
        while count<cc:  
            count+=1
            line = file.readline()
            s = line.split(",")
            marks.append([s[0],s[1]])
        file.close()
        
        avg = avg_calc(marks)
        SD = SD_calc(marks)
        lie = ""
        #checks if students are below DP
        for student in marks:
            tote = avg-SD
            mark = eval(student[1])
            if mark<tote:
                lie += student[0] + "\n"
        
        print("The average is:",("%0.2f" % avg))
        print("The std deviation is:",("%0.2f" %SD))
        if lie:
            print("List of students who need to see an advisor:")
            print(lie)
    
    except FileNotFoundError:
        print("Sorry, file not found")
    
    

def count_lines(filename):
    with open(filename) as file:
        return sum(1 for _ in file)

def avg_calc(array):
    u = 0
    count = 0
    for item in array:
        mark = eval(item[1])
        u += mark
        count +=1
    mean = round((u/count),2)
    return mean

def SD_calc(array):
    stand = 0
    count = 0
    mean = avg_calc(array)
    for item in array:
        mark = eval(item[1])
        stand += math.pow((mark-mean),2)
        count+=1
    dev = round((math.sqrt(stand/count)),2)
    return dev


main()