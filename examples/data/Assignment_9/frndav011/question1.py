"""Reading from text file
David Fransch
13-05-2014
""" 
import math
names = []
marks = [] 
#Open text file
enter = input("Enter the marks filename:\n")
f = open(enter, "r")
def s_marks(f, names, marks):
    # Re-arrange txt file and place file into list
    for line in f:
        name, mark = line.split(',')
        mark = eval(mark)# Marks are strings, so convert to ints
        names.append(name)
        marks.append(mark)
        
    avg = sum(marks)/len(marks)# Calculates average
    std = 0 
    y = 0
    x= ""
    
    #Calculates the standard deviation 
    for i in marks:
        y += ((i*1.0) -avg)**2
    std = math.sqrt(y/(len(marks)* 1.0))
    #Concert ints to strings
    n_avg =avg
    n_std =std
    #Round off to 2 decimal places
    av = "{0:.2f}".format(n_avg)
    st = "{0:.2f}".format(n_std)
    #Print out avg and standard deviation
    print("The average is:", av) 
    print("The std deviation is:", st)        
    #To get name of students whos marks are one standard deviation below the mean
    if len(marks) != 1:
        print("List of students who need to see an advisor:")
        for i in range (len (marks)):
            if (marks [i] < math.fabs (avg - std) ):
                print (names [i], sep ="")

          
           
s_marks(f,names, marks)
f.close()
