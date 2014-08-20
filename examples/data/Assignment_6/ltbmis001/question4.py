a=input("Enter a space-separated list of marks:\n")
b=a.split(" ")

top=0
second=0
third=0
fourth=0
fail=0

for i in b:
    i=eval(i)
    if i>=75:
        top+=1
    elif 70<=i<75:
        second+=1
    elif 60<=i<70:
        third+=1
    elif 50<=i<60:
        fourth+=1
    elif i<50:
        fail+=1
print("1 |"+"X"*top)
print("2+|"+"X"*second)
print("2-|"+"X"*third)
print("3 |"+"X"*fourth)
print("F |"+"X"*fail)
