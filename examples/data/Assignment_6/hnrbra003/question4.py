marks = input("Enter a space-separated list of marks:\n").split(" ")
first = 0
uppersecond = 0
lowersecond = 0
third = 0
fail = 0
for k in marks:
    if eval(k) > 100 or eval(k) < 0:
        print("Invalid")
    elif eval(k) > 75:
        first+=1
    elif eval(k) > 70:
        uppersecond+=1
    elif eval(k) > 60:
        lowersecond+=1
    elif eval(k) > 50:
        third+=1
    else:
        fail+=1
print("1 |","X"*first,sep='')
print("2+|","X"*uppersecond,sep='')
print("2-|","X"*lowersecond,sep='')
print("3 |","X"*third,sep='')
print("F |","X"*fail,sep='')