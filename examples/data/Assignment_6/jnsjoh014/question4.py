"""Assignment 6 Question 4
Johan Jansen van Vuuren (JNSJOH014)
21 April 2014"""

def main():
    marks = {"1":0,"2+":0,"2-":0,"3":0,"F":0}
    # Get marks as input and create a temporary array of marks
    marksInput = (input("Enter a space-separated list of marks:\n")).split(" ")
    marksInt = []
    for i in range(len(marksInput)):
        marksInt.append(eval(marksInput[i]))
    # Change dictionary keys as marks are processed
    for i in range(len(marksInput)):
        if(marksInt[i]>=75):
            marks["1"]+=1
        elif marksInt[i]>=70:
            marks["2+"]+=1
        elif marksInt[i]>=60:
            marks["2-"]+=1
        elif marksInt[i]>=50:
            marks["3"]+=1
        else:
            marks["F"]+=1
    #print(marks)
    print("1 |",marks["1"]*"X",sep="")
    print("2+|",marks["2+"]*"X",sep="")
    print("2-|",marks["2-"]*"X",sep="")
    print("3 |",marks["3"]*"X",sep="")
    print("F |",marks["F"]*"X",sep="")




if __name__=="__main__": main()