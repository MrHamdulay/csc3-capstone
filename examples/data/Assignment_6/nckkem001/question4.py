"""Program to draw a histogram of class mark data.
Kemeshan Naicker
23 April 2014"""

def histo():
    #Prompt user for marks.
    marks=input("Enter a space-separated list of marks:\n")
    #Convert string of marks into a list of integers
    marks=marks.split()
    for i in range(len(marks)):
        marks[i]=eval(marks[i])
    #Specificy accumulator variables for catagories.
    frst = 0
    uscnd = 0
    lscnd = 0
    thrd = 0
    fail = 0
    
    #Place marks in list into catagories.
    for i in marks:
        if i >= 75:
            frst += 1
        elif i >= 70:
            uscnd += 1
        elif i >= 60:
            lscnd += 1
        elif i >= 50:
            thrd += 1
        else:
            fail += 1
            
    #Print histogram.
    print("1 |", "X"*frst, sep = "")
    print("2+|", "X"*uscnd, sep = "")
    print("2-|", "X"*lscnd, sep = "")
    print("3 |", "X"*thrd, sep = "")
    print("F |", "X"*fail, sep = "")
    
if __name__=="__main__":
    histo()

