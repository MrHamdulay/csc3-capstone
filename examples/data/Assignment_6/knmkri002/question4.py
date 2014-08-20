"""program that takes a list of marks and outputs a historgram representation
Kristin Kinmont
20 April 2014"""

#get a list of marks
mark = input("Enter a space-separated list of marks:\n")
mark = mark.split(" ")
#count the number of marks in each UCT marks category
count1 = 0
count2upper = 0
count2lower = 0
count3 = 0
countF = 0
for i in mark:
    i = eval(i)
    if i >= 75:
        count1 += 1
    elif i >= 70:
        count2upper += 1
    elif i >= 60:
        count2lower += 1
    elif i >= 50:
        count3 += 1
    else:
        countF += 1
    
#print historgram
print("1 |","X"*count1,sep="")
print("2+|","X"*count2upper,sep="")
print("2-|","X"*count2lower,sep="")
print("3 |","X"*count3,sep="")
print("F |","X"*countF,sep="")