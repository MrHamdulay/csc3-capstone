#Tayla Radmore
#23 April 2014
#mark histogram

# getting input
marks=input("Enter a space-separated list of marks: \n")
list_of_marks=marks.split(" ")

#counting the marks
fail=0
third=0
lower_second=0
upper_second=0
first=0

for i in list_of_marks:
    i = eval(i)
    
   
    if 0<= i < 50:
        fail+=1
    if 50<= i <60:
        third+=1
    if 60<= i < 70:
        lower_second+=1
    if 70<= i <75:
        upper_second+=1
    if 75<= i <=100:
        first+=1
        
#printing the histogram
print("1 |","X"*first,sep="")
print("2+|","X"*upper_second,sep="")
print("2-|","X"*lower_second,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")