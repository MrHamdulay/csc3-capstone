# Yudhi Moodley
# Assignment 6 - Histogram and grade evaluator
#23/04/2014
   
marksList = [] 
grade = [0,0,0,0,0,]

def histogram():   
    
    marks = input("Enter a space-separated list of marks:\n") 
    marksList = marks.split(' ') 

# creating diagram in range of marks 
    for i in range (len(marksList)):
        if eval(marksList[i]) < 50:
            grade[0]+= 1
            
        elif 50<= eval(marksList[i]) < 60:
            grade[1]+=1
            
        elif 60<= eval(marksList[i]) < 70:
            grade[2]+=1
            
        elif 70<= eval(marksList[i]) < 75:
            grade[3]+=1
            
        elif eval(marksList[i]) >=75:
            grade[4]+=1

# matching output to input
    print("1 |"+"X"*grade[4])
    print("2+|"+"X"*grade[3])
    print("2-|"+"X"*grade[2])
    print("3 |"+"X"*grade[1])
    print("F |"+"X"*grade[0])

histogram()