''' Assignment 6, question 4
Histogram based on mark categories at UCT
Tristan Subroyen
19 April 2014 '''

def main():
    marksList = [] # initialize list
    # initialize array for mark range
    grades = [0,0,0,0,0,]

    marks = input("Enter a space-separated list of marks:\n") # ask user for input
    marksList = marks.split(' ') # split user input by space; add to list

    for i in range (len(marksList)): # loop for each element in marksList...
        # use of if/else statements to classify marks
        if eval(marksList[i]) < 50:
            grades[0]+= 1
        elif 50<= eval(marksList[i]) < 60:
            grades[1]+=1
        elif 60<= eval(marksList[i]) < 70:
            grades[2]+=1
        elif 70<= eval(marksList[i]) < 75:
            grades[3]+=1
        elif eval(marksList[i]) >=75:
            grades[4]+=1

    # Print the histogram, with axes and required results        
    print("1 |"+"X"*grades[4])
    print("2+|"+"X"*grades[3])
    print("2-|"+"X"*grades[2])
    print("3 |"+"X"*grades[1])
    print("F |"+"X"*grades[0])
    
if __name__ == '__main__':
    main()

        

