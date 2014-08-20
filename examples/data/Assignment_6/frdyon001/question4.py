"""Yonela Ford
make a list of mark and put into histogram
23 April"""

#GET MARKS FROM USER
marks=input("Enter a space-separated list of marks:\n")
mark=marks.split()
fail=0
third=0
lower_2=0
upper_2=0
first=0
# FOR EACH MARK INCREMENT APPROPRIATE CLASS
for i in mark:
    i=eval(i)
    if i<50:
        fail+=1
    elif 50<=i<60:
        third+=1
    elif 60<=i<70:
        lower_2+=1
    elif 70<=i<75:
        upper_2+=1
    elif 75<=i<=100:
        first+=1
#PRINT HISTOGRAM       
print("1 |","X"*first,sep="")
print("2+|","X"*upper_2,sep="")
print("2-|","X"*lower_2,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")

