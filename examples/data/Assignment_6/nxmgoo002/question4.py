'''this program ouputs a histogram of marks
Nxumalo Goodman
22 April 2014'''

def marks_histogram() :
    #create lists
    fail = []
    third = []
    lower = []
    upper = []
    first =[]
    
    marks = input("Enter a space-separated list of marks:\n")
    marks = marks.split(" ")
    
    #add the values to its list type
    for i in marks:
        a = int(i)
        if 0<= a < 50:
            fail.append(a)
        elif 50 <= a < 60:
            third.append(a)
        elif 60 <= a < 70:
            lower.append(a)
        elif 70 <= a < 75:
            upper.append(a)
        elif 75 <= a <= 100:
            first.append(a)
            
    #output of histogram
    print("1 |","X"*len(first),sep="")
    print("2+|","X"*len(upper),sep="")
    print("2-|","X"*len(lower),sep="")
    print("3 |","X"*len(third),sep="")
    print("F |","X"*len(fail),sep="")
    
marks_histogram()