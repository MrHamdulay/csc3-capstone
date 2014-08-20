"""Assignment 6 Q4 create a diagram
Nandani Birjanund
23/04/14"""

marks=input("Enter a space-separated list of marks:\n") #User input
array=marks.split(" ") #splitting the array

countf=0 #5 lists and counters
count3=0 
count2low=0
count2up=0
count1=0

for i in range(len(array)): #testing counters
    
    num=int(array[i]) #integer form of array
    
    if num<50: 
        countf+=1 #increasing count
    
    elif num>=50 and num<60:  
        count3+=1
        
    elif num>=60 and num<70:
        count2low+=1
        
    elif num>=70 and num<75:
        count2up+=1
        
    elif num>=75 and num<=100:
        count1+=1
        
print("1 |","X"*count1,sep="") #printing count 
print("2+|","X"*count2up,sep="")
print("2-|","X"*count2low,sep="")
print("3 |","X"*count3,sep="")
print("F |","X"*countf,sep="")
        