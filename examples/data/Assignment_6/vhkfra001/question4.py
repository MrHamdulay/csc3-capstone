# Assignment 6
# Program to take in marks and draw a histogram of them
# Frans van Hoek   
# 22 April 2014

def get_marks():
    marks = input("Enter a space-separated list of marks:\n")
    mlist = marks.split(" ")
    return mlist


def histogram(a):
    # Define the category counters
    first = 0
    second1 = 0
    second2 = 0
    third = 0
    fail = 0
    
    # Tally from list 'a'
    for i in a:
        
        if eval(i) >= 75:
            first += 1
            
        elif eval(i) >= 70:
            second1 += 1
            
        elif eval(i) >= 60:
            second2 += 1
            
        elif eval(i) >= 50:
            third += 1
            
        else:
            fail += 1
            
    # Now draw histogram
    print ("1 |" + first*"X")
    print ("2+|" + second1*"X")
    print ("2-|" + second2*"X")
    print ("3 |" + third*"X")
    print ("F |" + fail*"X")
    
def main():
    marks = get_marks()
    histogram(marks)
    
main()