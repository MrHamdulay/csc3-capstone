#Khyati Jinerdeb
#Assignment 6
#25 April 2014
#program taking a list of marks and output a histogram of marks according to mark categories

marks=input("Enter a space-separated list of marks:\n")
list_of_marks=marks.split(" ")

countF=0
count3=0
count2Lower=0
count2Upper=0
count1=0

for i in range(len(list_of_marks)):
    number=int(list_of_marks[i])
    
    if number<50:
        countF+=1
        
    elif number>=50 and number<60:
        count3+=1
        
    elif number>=60 and number<70:
        count2Lower+=1
        
    elif number>=70 and number<75:
        count2Upper+=1
        
    elif number>=75 and number<=100:
        count1+=1
        
print("1 |","X"*count1,sep="")
print("2+|","X"*count2Upper,sep="")
print("2-|","X"*count2Lower,sep="")
print("3 |","X"*count3,sep="")
print("F |","X"*countF,sep="")

    