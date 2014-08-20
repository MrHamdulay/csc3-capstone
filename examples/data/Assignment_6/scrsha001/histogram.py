#Shaaheen Sacoor SCRSHA001
#19 April 2014
#Program to print Histogram with entered marks

def main():
    marks = input("Enter a space-seperated list of marks:\n")
    marks_list = marks.split() #makes marks into list
    first = 0 #Variables to count the occurences of different categories of marks
    up_second=0
    low_second=0
    third=0
    fail=0    
    for i in range(len(marks_list)): #Goes through list
        cat = eval(marks_list[i]) #cat=category. variable assigned to current number in list
        if cat >=75: # Checks what category mark falls under and then adds 1 to specific category
            first +=1
        elif cat>=70:
            up_second +=1
        elif cat>=60:
            low_second +=1
        elif cat >=50:
            third+=1
        elif cat<50: 
            fail+=1
    print("1 |","X"*first,sep="")
    print("2+|","X"*up_second,sep="")
    print("2-|","X"*low_second,sep="")    
    print("3 |","X"*third,sep="")
    print("F |","X"*fail,sep="")            
main()