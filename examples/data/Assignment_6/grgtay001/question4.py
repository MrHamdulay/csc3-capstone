"""program that takes in a list of marks and outputs a histogram
Tayla George
23 april 2014"""


def histogram():
    marks = input("Enter a space-separated list of marks:\n")
    marks_sep = marks.split()
    
    Failcount = 0
    Thirdcount =0
    lower2ndcount =0
    upper2ndcount =0
    firstcount =0    
    
    for i in marks_sep:
        i =int(i) #converting each item in the list to an integer
        #if i<0 or i>100:
            #print(i," is invalid mark")
        if i>=75: #counting the number of 1sts
            firstcount +=1
        elif 70<=i<75: #counting the number of 2+
            upper2ndcount+=1
        elif 60<=i<70: #counting the number of 2-
            lower2ndcount+=1
        elif 50<=i<60: #counting the number of 3
            Thirdcount+=1
        else: #counting the number of fails
            Failcount+=1
            
    print("1 |",firstcount*"X",sep='')
    print("2+|",upper2ndcount*"X",sep='')
    print("2-|",lower2ndcount*"X",sep='')
    print("3 |",Thirdcount*"X",sep='')
    print("F |",Failcount*"X",sep='')

histogram()