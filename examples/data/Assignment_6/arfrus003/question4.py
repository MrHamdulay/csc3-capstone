#create graph function
def marks_histo():
    #all categories into which percentages fall
    fail = 0
    third = 0
    lower2nd = 0
    upper2nd = 0
    first = 0        
    
    input_percents = input("Enter a space-separated list of marks:\n")
    percentages = input_percents.split()
   
    for i in percentages:
        i =int(i) #make integer
        
        if i>=75: 
            first += 1 #number firsts
        
        elif 70<=i<75:
            upper2nd += 1 #number upper2nds
        
        elif 60<=i<70: 
            lower2nd += 1 #number lower2nds
        
        elif 50<=i<60: 
            third += 1 #number 3rds
        
        else: 
            fail += 1 #number fails
            
    print("1 |",first*"X",sep='')
    print("2+|",upper2nd*"X",sep='')
    print("2-|",lower2nd*"X",sep='')
    print("3 |",third*"X",sep='')
    print("F |",fail*"X",sep='')

marks_histo()