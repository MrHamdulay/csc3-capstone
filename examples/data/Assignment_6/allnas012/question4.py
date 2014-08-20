x=input("Enter a space-separated list of marks:\n")
marks=x.split(" ")

counter1=0
counter2a=0
counter2b=0
counter3=0
counter4=0


for mark in marks:
    if int(mark) < 50:
        counter4+=1
    elif 50 <= int(mark) <60:
        counter3+=1
    elif 60 <= int(mark) <70:
        counter2b+=1
    elif 70 <= int(mark) <75:
        counter2a+=1
    elif int(mark) >= 75:
        counter1+=1
        
print("1 |"+"X"*counter1)
print("2+|"+"X"*counter2a)
print("2-|"+"X"*counter2b)
print("3 |"+"X"*counter3)
print("F |"+"X"*counter4)
