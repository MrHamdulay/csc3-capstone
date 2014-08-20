"""Program to draw histogram using given list of marks
Dumisani J Nyathi
25-04-2014"""

def marks():
    x=input("Enter a space-separated list of marks:\n")
    
    y=x.split()
        
    fail=0
    third=0
    lower=0
    upper=0
    first=0
    for i in y:
        if eval(i)< 50:
            fail+=1
        elif eval(i)<60:
            third+=1
        elif eval(i)<70:
            lower+=1
        elif eval(i)<75:
            upper+=1
        elif eval(i)>=75:
            first+=1
            
    print("1 |","X"*first,sep="")
    print("2+|","X"*upper,sep="")
    print("2-|","X"*lower,sep="")
    print("3 |","X"*third,sep="")
    print("F |","X"*fail,sep="")

marks()