"""A program to output a histogram representation of the marks according to the mark categories at UCT
Simlindile Mahlaba
23 April 2014"""

def marks():
    x= input("Enter a space-separated list of marks:\n")
    list_of_marks=x.split(" ")
    final_list= []
    for i in list_of_marks:
        mark1=eval(i)
        final_list.append(mark1)
        fail=0
        third=0
        lower_second=0
        upper_second=0
        first=0
    for mark in final_list:
        if (mark>= 75):
            first += 1
        elif (mark >= 70):
            upper_second +=1
        elif (mark >= 60):
            lower_second +=1
        elif (mark >= 50):
            third +=1
        else:
            fail +=1
            
             
            
    print("1 |" , "X"*first ,"\n2+|" , "X"*upper_second , "\n2-|" , "X"*lower_second ,"\n3 |","X"*third ,"\nF |","X"*fail, sep="")
    
marks()
            
    