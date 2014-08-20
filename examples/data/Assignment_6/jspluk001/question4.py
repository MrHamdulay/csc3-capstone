# Luke Joseph
# Question 4 of assignment 6
# 2014-04-20
def histogram():
    a = input("Enter a space-separated list of marks:\n")
    x = a.split(" ")
    first=0
    hsecond=0
    lsecond=0
    third=0
    fail=0
    for i in range(len(x)): # converting percentage to symbol and counting number of occurrences
        if eval(x[i]) >= 75:
            first+=1
        elif eval(x[i])>=70:
            hsecond+=1
        elif eval(x[i])>=60:
            lsecond+=1
        elif eval(x[i])>=50:
            third+=1
        else:
            fail+=1
    print("1 |","X"*first,sep="") #producing outputs
    print("2+|","X"*hsecond,sep="")
    print("2-|","X"*lsecond,sep="")
    print("3 |","X"*third,sep="")
    print("F |","X"*fail,sep="")
histogram()