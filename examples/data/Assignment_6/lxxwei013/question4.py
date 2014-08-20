"""histogram representation of marks
21 April 2014
Michelle Lu"""

#Create lists
fail=[]
third=[]
lower=[]
upper=[]
top=[]

#enter the marks
marks=input("Enter a space-separated list of marks:\n")
marks=marks.split()

#assign marks to list
for i in marks:
    i=eval(i) #turn into integer
    if i<50:
        fail.append(i)
    elif 50<=i<60:
        third.append(i)
    elif 60<=i<70:
        lower.append(i)
    elif 70<=i<75:
        upper.append(i)
    elif 75<=i<=100:
        top.append(i)


#print out the histogram
print("1 |", "X"*len(top), sep="")
print("2+|", "X"*len(upper), sep="")
print("2-|","X"*len(lower), sep="")
print("3 |", "X"*len(third), sep="")
print("F |", "X"*len(fail), sep="")
