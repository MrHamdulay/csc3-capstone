#Kalind Ramnarayan
#23 April 2014
#Histogram from a list of marks

marks=input("Enter a space-separated list of marks:\n")
mylist=marks.split()
first=0
uppsecond=0
lowersecond=0
third=0
fail=0


for i in mylist:
    if eval(i)>=75:
        first+=1
        
    elif eval(i)>=70:
        uppsecond+=1
        
    elif eval(i)>=60:
        lowersecond+=1
        
    elif eval(i)>=50:
        third+=1
        
    else:
        fail+=1

print("1 |","X"*first, sep="")

print("2+|","X"*uppsecond, sep="")

print("2-|","X"*lowersecond, sep="")

print("3 |","X"*third, sep="")

print("F |","X"*fail, sep="")
        
        