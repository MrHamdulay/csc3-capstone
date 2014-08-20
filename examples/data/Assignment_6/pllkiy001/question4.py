#program to create histogram
#kiyarah pillay
#24 april 2014

#user inputs marks as a string
entries=input("Enter a space-separated list of marks:\n")
#marks are entered into a list by splitting string into list of marks using " "(space) as a separater
marks_list=entries.split(" ")

#variables to count each category of marks are defined
first=0
second_up=0
second_low=0
third=0
fail=0

#loops through the list of marks
for i in range(len(marks_list)):

#converts marks from string into integer values    
    mark=int(marks_list[i])
    
    if mark<=100 and mark>=75:
#category 'first' increases by 1 if current mark is between 75 and 100
        first+=1
    elif mark <75 and mark>=70:
#category 'second_up' increases by 1 if current mark is between 70 and 75
        second_up+=1
    elif mark<70 and mark>=60:
#category'second_low' increasesby 1 if current mark is between60 and 70
        second_low+=1
    elif mark<60 and mark>=50:
#category'third' increases by 1 if current mark is between 50 and 60
        third+=1
#category 'fail'increases by 1 if current mark is less than 50   
    else:
        fail+=1
        
#prints histogramby multiplying 'X'by the each category
print("1 |","X"*first,sep="")
print("2+|","X"*second_up,sep="")
print("2-|","X"*second_low,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")
    