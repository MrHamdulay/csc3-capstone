# Yentl Naidu (NDXYEN001)
# 24 April 2014
# Assignment 6
# Question 4

# Show the counters list   
counters=[0,0,0,0,0]

# Get the input
entMarks=input("Enter a space-separated list of marks:\n")

# Putting the marks into catergories
marks=entMarks.split()
for i in range(len(marks)):
    currMark=eval(marks[i])
    if(currMark>=75):
        counters[0]+=1
    elif(70<=currMark<75):
        counters[1]+=1
    elif(60<=currMark<70):
        counters[2]+=1
    elif(50<=currMark<60):
        counters[3]+=1
    else:
        counters[4]+=1

# Print the histogram
print("1 |"+(counters[0]*"X")+"\n2+|"+(counters[1]*"X")+"\n2-|"+(counters[2]*"X")+"\n3 |"+(counters[3]*"X")+"\nF |"+(counters[4]*"X"))