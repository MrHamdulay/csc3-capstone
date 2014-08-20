"""Tevin Chetty
22 April 2014
Program to draw a graph showing class marks"""

marks=input("Enter a space-separated list of marks: \n")

list_marks=marks.split(" ") #creates a list from the input

#have to define 0 to add to it later in the for loop
fail=0
third=0
u_second=0
l_second=0
first=0


for i in list_marks: #to find the length of each bar
    y=eval(i)
    if y >= 75:
        first += 1
    elif y>=70 and y<75:
        u_second += 1
    elif y>=60 and y<70:
        l_second += 1    
    elif y>=50 and y<60:
        third += 1
    elif y<50:
        fail += 1
#to print the histogram        
print("1 |","X"*first, sep="")
print("2+|","X"*u_second, sep="")
print("2-|","X"*l_second, sep="")
print("3 |","X"*third, sep="")
print("F |","X"*fail, sep="")