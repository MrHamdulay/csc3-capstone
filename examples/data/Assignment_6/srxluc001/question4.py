
marks=input("Enter a space-separated list of marks:\n")
mark_list=marks.split(" ")

fail=0
third=0
first=0
upper2nd=0
lower2nd=0
for i in mark_list:
    x=eval(i)
    if x <50:
        fail+=1
    elif 50<=x<60:
        third+=1
    elif 60<=x<70:
        lower2nd=+1
    elif 70<=x<75:
        upper2nd=+1
    elif x>=75:
        first+=1
    
print("1 |",end="")
print(first*"X")
print("2+|",end="")
print(upper2nd*"X")
print("2-|",end="")
print(lower2nd*"X")
print("3 |",end="")
print(third*"X")
print("F |",end="")
print(fail*"X")


    

