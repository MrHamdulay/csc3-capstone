'''Hstogram plotter
Sbongakonke Mlangeni
23 April 2014'''

def xy():
    #initializing all the counts
    failCount = 0
    thirdCount = 0
    LowersecondCount = 0
    UppersecondCount = 0
    FirstCount = 0
    
    #taking input
    x = input('Enter a space-separated list of marks:\n')
    
    #crearing a list
    x = x.split(' ')
    
    for i in x:
        #setting conditions for the histogram
        a = eval(i)
        if a < 50:
            failCount += 1
        elif 50 <= a < 60:
            thirdCount += 1
        elif 60 <= a < 70:
            LowersecondCount += 1
        elif 70 <= a < 75:
            UppersecondCount += 1
        elif a >= 75:
            FirstCount += 1
            
    #Printing out the histogram
    print('1 |'+('X' * FirstCount))
    print('2+|'+('X' * UppersecondCount))
    print('2-|'+('X' * LowersecondCount))
    print('3 |'+('X' * thirdCount))
    print('F |'+('X' * failCount))
    
xy()