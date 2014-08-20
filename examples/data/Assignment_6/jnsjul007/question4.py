#Program to print histogram of marks
#Julian van Rensburg
#24 April 2014
y=input("Enter a space-separated list of marks:\n")
X=y.split(' ')
x=[]
for item in X:
    x.append(int(item))
count1 = 0
count2=0
count3=0
count4=0
count5=0
for item in x:
    if 0<=item<50:
        count1+=1
    if 50<=item<60:
        count2+=1
    if 60<=item<70:
        count3+=1
    if 70<=item<75:
        count4+=1
    if 75<=item:
        count5+=1
print("1 |","X"*count5, sep='')
print("2+|","X"*count4,sep='')
print("2-|","X"*count3,sep='')
print("3 |","X"*count2,sep='')
print("F |","X"*count1,sep='')
        
    
            

    
