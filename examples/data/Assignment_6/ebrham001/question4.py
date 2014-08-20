'''Program that takes a list of marks and outputs a histogram of the marks
HAMZA EBRAHIM
25/04/14'''

# Assignment 6 - Question 4


# define marks function

def marks():
    
    # prompt user for marks input separated by a space
    
    x = input("Enter a space-separated list of marks:\n").split(" ")
    
    # initialize grades list, convert marks from string to integer and append to grades list
    
    grades = []
    
    for i in x:
        grades.append(eval(i))
    return grades

# define histogram representation function

def graph():
    
    x = marks()
    
    z, y, b, m, n = 0, 0, 0, 0, 0
    
    
    # assign marks to class 
    
    for i in x:
        if i < 50:
            z = z + 1
        
        elif 50<=i<60:
            y = y + 1
        
        elif 60<=i<70:
            b = b + 1
        
        elif 70<=i<75:
            m = m + 1
        
        elif i >=75:
            n = n + 1
    
    # prints histogram representation of marks
            
    print("1 ", "|",  "X" * n,  sep="")
    print("2+", "|", "X" * m, sep="")
    print("2-", "|", "X" * b, sep="")
    print("3 ", "|",  "X" * y,  sep="")
    print("F ", "|",  "X" * z,  sep="")
    
    # program ends
graph()    