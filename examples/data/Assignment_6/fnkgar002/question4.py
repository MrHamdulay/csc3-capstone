"""program that takes in a list of marks and outputs a histogram representation of the marks according to UCT mark categories
Gary Finkelstein
22 April 2014"""

#allow user to input marks
input_marks = input("Enter a space-separated list of marks:\n")
#put marks into array by spliting on a space
Mark = input_marks.split(" ")
#create a blank array to store catorgory values
numMarks = []

#function catorgory() is used to add a value to the blank array according to the value entered by the user. the occurances of this values are then counted and printed
def Catorgory():
    for i in range(len(Mark)):
        
        if int(Mark[i]) < 50:
            numMarks.append(50)
        elif int(Mark[i]) < 60:
            numMarks.append(60)    
        elif int(Mark[i]) < 70:
            numMarks.append(70)    
        elif int(Mark[i]) < 75:
            numMarks.append(75)
        elif int(Mark[i]) <= 100:
            numMarks.append(100)
    fir = numMarks.count(100)
    sec1 = numMarks.count(75)
    sec2 = numMarks.count(70)
    third = numMarks.count(60)
    fail = numMarks.count(50)

    print("1 |"+"X"*fir)
    print("2+|"+"X"*sec1)
    print("2-|"+"X"*sec2)
    print("3 |"+"X"*third)
    print("F |"+"X"*fail)
#calling the category function
Catorgory()