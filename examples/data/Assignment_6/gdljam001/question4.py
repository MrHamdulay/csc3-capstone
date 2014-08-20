"""Sorting of marks into categories
James Godlonton
24 April 2014"""

def getMarks():#Function get marks input and prints a histogram of distribution  over categories
    newMark=input("Enter a space-separated list of marks:\n").split(" ")#gets marks input then splits into array
    countCateg=[0,0,0,0,0]#Array to count each category
    for mark in newMark: #Goes through all marks and adds one to the appropriate category for each mark
        inMark=int(mark)
        if(inMark>=75 and inMark<=100):
            countCateg[0]+=1
        elif(inMark>=70):
            countCateg[1]+=1
        elif(inMark>=60):
            countCateg[2]+=1
        elif (inMark>=50):
            countCateg[3]+=1
        elif(inMark<=50 and inMark>=0):
            countCateg[4]+=1
            
    print("1 |"+"X"*countCateg[0])#Printing histogram with X for each value in the count
    print("2+|"+"X"*countCateg[1])
    print("2-|"+"X"*countCateg[2])
    print("3 |"+"X"*countCateg[3])
    print("F |"+"X"*countCateg[4])
    
if __name__=="__main__":
    getMarks()
    
        