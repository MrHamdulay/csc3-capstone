#Create empty list and dictionary
marks = []
num ={}

#Get I/P
mark = input("Enter a space-separated list of marks:\n")
marks = mark.split(" ")

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
          
for i in range(len(marks)):
    if int(marks[i]) >= 75:
        count1 +=1
    elif int(marks[i]) >= 70:
        count2 +=1
    elif int(marks[i]) >= 60:
        count3 +=1
    elif int(marks[i]) >= 50:
        count4 +=1
    elif int(marks[i]) <50:
        count5 +=1
        
print("1 |",count1 *'X', sep="")
print("2+|",count2 *'X', sep="")
print("2-|",count3 *'X', sep="")
print("3 |",count4 *'X', sep="")
print("F |",count5 *'X', sep="")


        
        
        
        