"""program to plot a histogram
sarayn subroyen
24 april 2014"""


def histogram():
    marks = input("Enter a space-separated list of marks:\n")
    marks_sep = marks.split()
    
    #initial values
    Failcount = 0
    Thirdcount =0
    lower2ndcount =0
    upper2ndcount =0
    firstcount =0    
    
    for i in marks_sep:
        i =int(i)              #converting to integer
        
        if i>=75:              #counting 1sts
            firstcount +=1
        elif 70<=i<75:         #counting  2+
            upper2ndcount+=1
        elif 60<=i<70:         #counting  2-
            lower2ndcount+=1
        elif 50<=i<60:         #counting 3
            Thirdcount+=1
        else:                  #counting fails
            Failcount+=1
     
     
    #print histogram       
    print("1 |",firstcount*"X",sep='')
    print("2+|",upper2ndcount*"X",sep='')
    print("2-|",lower2ndcount*"X",sep='')
    print("3 |",Thirdcount*"X",sep='')
    print("F |",Failcount*"X",sep='')

histogram()