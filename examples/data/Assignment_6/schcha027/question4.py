#Charles Schleich SCHCHA027
#Question 4 Assignment 6
#defining variables
sentence=input("Enter a space-separated list of marks:\n")
marks_array=[]
marks_array=sentence.split()
marks_array.sort()
fail,third,lowerSec,upperSec,first=0,0,0,0,0

#for loop that counts each input set
for i in range(len(marks_array)):
    if eval(marks_array[i])<50:
        fail+=1
    elif 50<=eval(marks_array[i])<60:
        third+=1
    elif 60<=eval(marks_array[i])<70:
        lowerSec+=1    
    elif 70<=eval(marks_array[i])<75:
        upperSec+=1   
    elif 75<=eval(marks_array[i])<=100:
        first+=1
# final outputs the lazy way   
print("1 |","X"*first,sep="")
print("2+|","X"*upperSec,sep="")
print("2-|","X"*lowerSec,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")
