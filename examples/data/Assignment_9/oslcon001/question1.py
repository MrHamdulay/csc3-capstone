# analyses student marks read in from a file and determine which students need to see a student advisor
# Conor O'Sullivan
# 10/05/2014

import math

# Main function: promps user for file name and reads file
def main():
       filename = input("Enter the marks filename:\n")
       infile = open(filename, "r")
       
       #Spliting test file into names and marks
       names = []
       marks = []
       rec = infile.readlines()
       for line in rec:
              line = line.split(",")
              names.append(line[0])
              marks.append(eval(line[1]))
              
       average = avg(marks)
       S_Dev = std_dev(marks, average)
       
       print("The average is: " + "{0:0.2f}".format(average))
       print("The std deviation is: " + "{0:0.2f}".format(S_Dev))
       
       valid = True
       for pos in range(len(marks)):
              if check_adv(marks[pos], average, S_Dev) == True:
                     if valid == True:
                            print("List of students who need to see an advisor:")
                            valid = False
                     print(names[pos])
                     
       
       infile.close()
       

       
# Calculates Average
def avg(marks):
       average = 0
       for mark in marks:
              average += mark
       
       average = average/len(marks)
       return average
       
# Calculates the standard deviation of the marks
def std_dev(marks, avg):
       
       S_Dev = 0
       for mark in marks:
              S_Dev += (mark-avg)**2
       
       S_Dev = math.sqrt(S_Dev/len(marks))
       return S_Dev

# Checks to see if student needs an advisor
def check_adv(mark, average, S_Dev):      
       if mark < (average- S_Dev):
              return True
       return False
       
       
main()


