# question4.py
# program that outputs a histogram of marks entered by user according to UCT standards
# camilla craven
# 22 april 2014

marks = input("Enter a space-separated list of marks:\n") 
List = marks.split() # splits list of marks entered by each space between them
List = map(int, List) # converts strings in list to integers

fail, third, lower_2nd, upper_2nd, first = 0,0,0,0,0 # setting count of each class to 0

for mark in List:
    
    # add count to fail if mark between 0 and 50
    if 0<=mark<50:
        fail += 1
    # add count to third if mark between 50 and 60    
    elif 50<=mark<60:
        third += 1
    # add count to lower 2nd if mark between 60 and 70   
    elif 60<=mark<70:
        lower_2nd += 1
    # add count to upper 2nd if mark between 70 and 75    
    elif 70<=mark<75:
        upper_2nd +=1
    # add count to first if mark between 75 and 100  
    elif 75<=mark<=100:
        first += 1
    # sets restrictions    
    else:
        None
        
# histogram        
print("1 |", "X"*first, sep = "")
print("2+|", "X"*upper_2nd, sep = "")
print("2-|", "X"*lower_2nd, sep = "")
print("3 |", "X"*third, sep = "")
print("F |", "X"*fail, sep = "")