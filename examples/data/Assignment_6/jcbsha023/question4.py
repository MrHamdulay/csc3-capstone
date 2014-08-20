#program that outputs histogram
#Anthony Jacob
#24 April 2014


def histogram():
    # creating 5 different classes of marks
    first=0
    upper_second=0
    lower_second=0
    third=0
    fail=0    
    
    #asking user for list of marks and splitting them into individual grades
    mark=input("Enter a space-separated list of marks:\n")
    marks=mark.split(" ")
    
    #loop to go through grades and check which class it fall into
    for grade in marks:
        if eval(grade) < 50:
            fail+=1
        elif 50<= eval(grade) < 60:
            third+=1
        elif 60<= eval(grade) < 70:
            lower_second+=1
        elif 70<= eval(grade) < 75:
            upper_second+=1
        elif eval(grade) >= 75:
            first+=1
            
    #printing the histogram by multiplying the different "classes" by "X"
    print("1 |"+first*"X") 
    print("2+|"+upper_second*"X")
    print("2-|"+lower_second*"X")
    print("3 |"+third*"X")
    print("F |"+fail*"X")
            

histogram()  #calling the histogram function   