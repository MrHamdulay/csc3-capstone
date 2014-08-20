# Program outputsa histogram representation of marks
# Wandile Lesejane
# 20 April 2014

marks=input("Enter a space-separated list of marks:\n")
marks=marks.split(" ")
# lists of categories
fail=[]
third=[]
lower2=[]
upper2=[]
first=[]
# counters for lists
cf=0
c3=0
c2l=0
c2u=0
c1=0
# loop that categorises each mark
for i in marks:
    i=eval(i)
    if i<50:
        fail.append(i)
        cf+=1
    elif 50<=i<60:
        third.append(i)
        c3+=1
    elif 60<=i<70:
        lower2.append(i)
        c2l+=1
    elif 70<=i<75:
        upper2.append(i)
        c2u+=1
    else:
        first.append(i)
        c1+=1
# histogram with horizontal bars using "X"        
print("1 |",c1*'X',sep='')
print("2+|",c2u*'X',sep='')
print("2-|",c2l*'X',sep='')
print("3 |",c3*'X',sep='')
print("F |",cf*'X',sep='')