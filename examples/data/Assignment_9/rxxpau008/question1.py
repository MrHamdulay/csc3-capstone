#Description: Analyse student marks from a file and deterrmines which students need to see a student advisor
#Name: Paul Roux - RXXPAU008
#Date: 15 May 2014

import math

def open_file():
    """Reads the contents of a file and stores it in a list"""
    try:#Used in case the user enters a filename that doesn't exist
        name = input("Enter the marks filename:\n")
        f = open(name)
        for i in f.readlines():
            records.append(i)
        f.close()
        return True
    except:
        print("File not found")
        
def calc_average():
    """Calculates the average mark of th estudents from the marks in the file"""
    total = 0
    count = 0
    for i in records:
        total+=int(i[i.find(',')+1:])
        count+=1
    average = total/count
    return average
    
def calc_std_deviation(average):
    """Calculates the standard deviation"""
    sqr_sum = 0
    count = len(records)
    for i in records:
        value = int(i[i.find(',')+1:])
        sqr_sum+=(value-average)**2   
    std_deviation = math.sqrt(sqr_sum/count)
    return std_deviation
    
def req_advisor(std_deviation):
    """Outputs the names of the students who need to see a student advisor due to the fact their mark is below one standard deviation from the average"""
    students = []
    for i in records:
        if int(i[i.find(',')+1:]) < std_deviation:
            students.append(i[:i.find(',')])
    if students != []:
        print("List of students who need to see an advisor:")
        for i in students:
            print(i)
        
if __name__ == '__main__':
    records = []
    if open_file():#Only runs the code if a file is found
        avg = calc_average()
        stdev = calc_std_deviation(avg)
        one_deviation = avg-stdev
        print("The average is:","{0:.2f}".format(avg))
        print("The std deviation is:","{0:.2f}".format(stdev))
        req_advisor(one_deviation)