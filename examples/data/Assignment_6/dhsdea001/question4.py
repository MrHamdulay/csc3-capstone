#Question 4
#Producing a mark histogram
#By:Dean de Haast

def main():
    first=0
    second_U =0
    second_L=0
    third=0
    fail=0
    marks=[]
#Getting the marks
    marks_list = input("Enter a space-separated list of marks:\n")
#Inserting the marks into a list
    marks=marks_list.split()
#Sorting the marks into the correct catagory
    for i in range (len(marks)):
        if eval(marks[i])< 50:
            fail +=1
        elif eval(marks[i])<60:
            third +=1
        elif eval(marks[i])< 70:
            second_L +=1
        elif eval(marks[i])<75:
            second_U +=1
        elif eval(marks[i])>=75:
            first +=1
#Printing the results           
    print("1 |",first*"X",sep="")
    print("2+|",second_U*"X",sep="")
    print("2-|",second_L*"X",sep="")
    print("3 |",third*"X",sep="")
    print("F |",fail*"X",sep="")
main()
    
            
            
            
    