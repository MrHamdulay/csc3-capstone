# 2nd5 April 2nd014
# Shaun Muzenda
# program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks

def histogram():
    
    marks = input("Enter a space-separated list of marks:\n")
    marks_lst = marks.split()
    
    #setting count of each mark category to 0
    
    number_of_failures = 0      #number of students who failed
    number_third_pass = 0       #number of students who got third level pass
    number_lower2nd_pass = 0    #number of students who got lower 2nd pass
    number_upper2nd_pass = 0    #number of students who got upper 2d pass
    number_first_pass = 0       #number of students who got a first pass
    
    #loop to place and count the inputed marks in their appropriate range
    
    for i in marks_lst:
        i = int(i)                   
        if i >= 75:                   
            number_first_pass += 1
        elif 70 <= i < 75:              
            number_upper2nd_pass += 1
        elif 60 <= i < 70:              
            number_lower2nd_pass += 1
        elif 50 <= i < 60:              
            number_third_pass += 1
        else:                       
            number_of_failures += 1
     
     
    #drawing the histogram
    
    print("1 |",number_first_pass * "X",sep='')
    print("2+|",number_upper2nd_pass * "X",sep='')
    print("2-|",number_lower2nd_pass * "X",sep='')
    print("3 |",number_third_pass * "X",sep='')
    print("F |",number_of_failures * "X",sep='')

histogram()