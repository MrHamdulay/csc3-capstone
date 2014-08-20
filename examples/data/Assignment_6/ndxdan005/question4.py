marks=input("Enter a space-separated list of marks:\n")
mark=marks.split(" ")
fail=0
third=0
lower_second=0
upper_second=0
first=0
for element in mark:
    if int(element)<50:
        fail+=1
    elif int(element)<60:
        third+=1
    elif int(element)<70:
        lower_second+=1
    elif int(element)<75:
        upper_second+=1
    elif int(element)>=75:
        first+=1
print("1 |" + "X"*first,sep="")
print("2+|" + "X"*upper_second,sep="")
print("2-|" + "X"*lower_second,sep="")
print("3 |" + "X"*third,sep="")
print("F |" + "X"*fail,sep="")
