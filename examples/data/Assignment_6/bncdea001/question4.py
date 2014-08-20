#Question 4, Assignment 6
#Histogram for marks
#Dean Bunce
#21 April


def main():
    
    #Get the input of marks
    marks_string=input("Enter a space-separated list of marks: \n")
    
    #Store the marks in a list
    marks_list=marks_string.split()
    #print(marks_list)
    
    
    grade_list=[]
    #Iterate through the list and sort the marks
    for mark in marks_list:
        mark=eval(mark)
        if 75<=mark<=100:
            grade_list.append("1")
            
        elif mark>=70:
            grade_list.append("2+")
      
        elif mark>=60:
            grade_list.append("2-")
        
        elif mark>=50:
            grade_list.append("3")
            
        elif mark<50:
            grade_list.append("F")
            
    def bars(n):
        print("{0:<2}".format(n),"|", "X"*grade_list.count(n),sep="")
    
    bars("1")
    bars("2+")
    bars("2-")
    bars("3")
    bars("F")




            

main()    