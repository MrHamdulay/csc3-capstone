

marks=input("Enter a space-separated list of marks:\n")

histo=marks.split(" ")
fail=0
third=0
lower_second=0
upper_second=0
first=0


for i in range(len(histo)):
        mark=eval(histo[i])
        if mark < 50 :
                fail+=1
        if 50 <= mark <60:
                third +=1
        
        if 60<= mark <70:
                lower_second+=1
        
        if 70<= mark < 75:
                upper_second+=1
        
        if mark>=75:
                first+=1
        

print("1 |","X"*first,sep="")
print("2+|","X"*upper_second,sep="")
print("2-|","X"*lower_second,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")
        
        

    