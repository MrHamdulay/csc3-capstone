""" Histogram representation of marks
Kumaran Reddy
25 April 2014 """

#Create the list of marks
marks=input("Enter a space-separated list of marks:\n")
list=marks.split()
list.sort()

#Create the categories
First=[]
Second_upper=[]
Second_lower=[]
Third=[]
Fail=[]

#Sort marks into categories
for i in list:
    if 75 <= int(i) <= 100:
        First.append(i)
    elif 70 <= int(i) < 75:
        Second_upper.append(i)
    elif 60 <= int(i) < 70:
        Second_lower.append(i)
    elif 50 <= int(i) < 60:
        Third.append(i)
    else:
        Fail.append(i)
        
print("1 |"+"X"*len(First))
print("2+|"+"X"*len(Second_upper))
print("2-|"+"X"*len(Second_lower))
print("3 |"+"X"*len(Third))
print("F |"+"X"*len(Fail))
        
        