"""classify marks into mark categories
blessings hadebe
20 april 2014"""

marks= input("Enter a space-separated list of marks:\n")
marks=marks.split(" ")

firsts=[]
USecs=[]
LSecs=[]
thirds=[]
fails=[]

for i in marks:
    i=eval(i)
    if i>=75:
        firsts.append("X")
    elif i>=70:
        USecs.append("X")
    elif i>=60:
        LSecs.append("X")
    elif i>=50:
        thirds.append("X")
    else:
        fails.append("X")
        
print("1 |" , "".join(firsts), sep="")
print("2+|" , "".join(USecs), sep="")  
print("2-|" , "".join(LSecs), sep="")
print("3 |" , "".join(thirds), sep="")
print("F |" , "".join(fails), sep="")