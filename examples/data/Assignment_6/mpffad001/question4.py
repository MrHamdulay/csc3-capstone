'''a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks 
fadzai mupfunya
23/04/14'''

#to store all the marks entered
mark=[]
marks=input("Enter a space-separated list of marks:\n")
mark.append(marks)
mark=marks.split()

#to store the counters 
one=0
third=0
second_lower=0
second_upper=0
fail=0
for i in mark:
    if int(i)<50:
        fail+=1
    elif 50 <= int(i) < 60:
        third+=1
    elif 60 <= int(i) < 70:
        second_lower+=1
    elif 70 <= int(i) < 75:
        second_upper+=1
    elif int(i) >= 75:
        one+=1
#to print the key
print("1 |"+"X"*one)
print("2+|"+"X"*second_upper)
print("2-|"+"X"*second_lower)
print("3 |"+"X"*third)
print("F |"+"X"*fail)


