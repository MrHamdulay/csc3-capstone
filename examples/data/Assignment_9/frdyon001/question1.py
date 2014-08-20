"""program to analyse student marks read in from a file and determine which students need to see a student advisor
Yonela Ford
11 May 2014"""

import math
#get the file with which we must work
filename=input("Enter the marks filename:\n")


#make a mean
def mean():
    infile=open(filename,"r")
    summ=0
    count=0
    for line in infile:
        name,mark=line.split(",")
        summ+=eval(mark)
        count+=1
    return (summ/count)
    infile.close()


#make a standard deviation from the marks
def std_deviation():
    infile=open(filename,"r")
    add=0
    count=0
    for line in infile:
        name,mark=line.split(",")
        add+=(eval(mark)-mean())**2
        count+=1
        
    return math.sqrt((add/count))
    infile.close()
    
def main():
    #call the mean and std_deviation functions with the appropriate print statements
    print("The average is:","{0:.2f}".format(mean()))
    print("The std deviation is:", "{0:.2f}".format(std_deviation()))
    std_deviation()
    #check which students are below one standard deviation and print their names to see the student counsellor
    if std_deviation()>0:
        print("List of students who need to see an advisor:")
        infile=open(filename,"r")
        for line in infile:
            name,mark=line.split(",")
            bar=mean()-std_deviation()
            if eval(mark)<bar:
                print(name)
main()