counters=[0,0,0,0,0]
enterMarks=input("Enter a space-separated list of marks:\n")
marks=enterMarks.split()
for i in range(len(marks)):
    currentMark=eval(marks[i])
    if(currentMark>=75):
        counters[0]+=1
    elif(70<=currentMark<75):
        counters[1]+=1
    elif(60<=currentMark<70):
        counters[2]+=1
    elif(50<=currentMark<60):
        counters[3]+=1
    else:
        counters[4]+=1
print("1 |"+(counters[0]*"X")+"\n2+|"+(counters[1]*"X")+"\n2-|"+(counters[2]*"X")+"\n3 |"+(counters[3]*"X")+"\nF |"+(counters[4]*"X"))