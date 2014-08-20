'''Program program that takes in a list of marks and outputs a histogram representation 
Raeesa Behardien
BHRRAE003
Assignment 6
Question 4'''

#histogram programme
def histogram():
    marks = input("Enter a space-separated list of marks:\n")
    marks_sep = marks.split()
    
    Fail_count = 0
    Third_count =0
    lower_2nd_count =0
    upper_2nd_count =0
    first_count =0    
    
    for i in marks_sep:
        i =int(i) #converting items in list to integers
        if i>=75: #counting the 1sts
            first_count +=1
        elif 70<=i<75: #counting the 2+
            upper_2nd_count+=1
        elif 60<=i<70: #counting the 2-
            lower_2nd_count+=1       
        elif 50<=i<60: #counting the 3
            Third_count+=1
        else: #counting fails
            Fail_count+=1
            
    print("1 |",first_count*"X",sep='')
    print("2+|",upper_2nd_count*"X",sep='')
    print("2-|",lower_2nd_count*"X",sep='')
    print("3 |",Third_count*"X",sep='')
    print("F |",Fail_count*"X",sep='')

histogram() #call histogram function