#generate a histogram from inputed marks
#wayne de jager
#24 april 2014

marksgiven=input("Enter a space-separated list of marks:\n")
marklist=marksgiven.split(" ")

#calculating number of attributes per category
first=0  
upper=0
lower=0
third=0
fail=0
for i in range(0,len(marklist)):
    mark=eval(marklist[i])
    if mark>=75:
        first=first+1
    elif mark<75 and mark>=70:
        upper=upper+1
    elif mark<70 and mark>=60:
        lower=lower+1
    elif mark<60 and mark>=50:
        third=third+1
    else: fail=fail+1

#print histogram
print("1 |","X"*first,sep="")
print("2+|","X"*upper,sep="")
print("2-|","X"*lower,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")