#GLMSUM001
#Sumayah Goolam Rassool
#23 April 2014

marks=input("Enter a space-separated list of marks:\n")
array=marks.split(" ")

countf=0
count3=0
count2low=0
count2up=0
count1=0

for i in range(len(array)):
    
    num=int(array[i])
    
    if num<50:
        countf+=1
        
    elif num>=50 and num<60:
        count3+=1
        
    elif num>=60 and num<70:
        count2low+=1
        
    elif num>=70 and num<75:
        count2up+=1
        
    elif num>=75 and num<=100:
        count1+=1
        
print("1 |","X"*count1,sep="")
print("2+|","X"*count2up,sep="")
print("2-|","X"*count2low,sep="")
print("3 |","X"*count3,sep="")
print("F |","X"*countf,sep="")
        