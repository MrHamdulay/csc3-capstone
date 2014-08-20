#MZWNIC001/Nicholas Mazower    
#25/04/2014
#UCT mark histogram-er

marks=input("Enter a space-separated list of marks:\n").split(" ")
#initialising all the mark categories
fail=0
third=0
lower_2nd=0
upper_2nd=0
first=0

for a in marks:
    a=eval(a)
    if a<50:
        fail+=1
    elif 50<=a<60:
        third+=1
    elif 60<=a<70:
        lower_2nd+=1
    elif 70<=a<75:
        upper_2nd+=1
    elif 75<=a:
        first+=1
print("1 |","X"*first, sep="")      
print("2+|","X"*upper_2nd, sep="")
print("2-|","X"*lower_2nd, sep="")
print("3 |","X"*third, sep="")
print("F |","X"*fail, sep="")