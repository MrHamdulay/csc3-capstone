# Litha Maqungo
#Assignment 6: question 4
# 24 April 2014

mark=input("Enter a space-separated list of marks:\n") #the original input
totalmarks=mark.split(" ")
percentage50,percentage60,percentage70,percentage75,percentage80=0,0,0,0,0 #the opening values
for i in totalmarks:
    x=eval(i) #changing from a string
    if 0<=x<50: #adding to count for marks in that range
        percentage50+=1
    elif 50<=x<60:
        percentage60+=1
    elif 60<=x<70:
        percentage70+=1
    elif 70<=x<75:
        percentage75+=1
    elif 75<=x<=100:
        percentage80+=1
        
print("1 |","X"*percentage80,sep="") #outputting the outcomes of all the data
print("2+|","X"*percentage75,sep="")
print("2-|","X"*percentage70,sep="")
print("3 |","X"*percentage60,sep="")
print("F |","X"*percentage50,sep="")