"""Program to output histogram of marks
Tyrone Arnold
24/-4/2014"""

def mark_histogram():
    
    result=input("Enter a space-separated list of marks:\n")
    result=result.split()
    
    
    first_quartile=0
    lower_second=0
    upper_second=0
    third_quartile=0
    Fail_count=0
    
    for i in range(len(result)):
        if int(result[i-1])<50:
            Fail_count+=1
        elif 50<=int(result[i-1])<60:
            third_quartile+=1
        elif 60<=int(result[i-1])<70:
            lower_second+=1
        elif 70<=int(result[i-1])<75:
            upper_second+=1
        elif 75<=int(result[i-1]):
            first_quartile+=1
            
    
    print("1 |","X"*first_quartile, sep="")
    print("2+|", "X"*upper_second, sep="")
    print("2-|", "X"*lower_second,sep="")
    print("3 |","X"*third_quartile,sep="")
    print("F |","X"*Fail_count,sep="")
mark_histogram()