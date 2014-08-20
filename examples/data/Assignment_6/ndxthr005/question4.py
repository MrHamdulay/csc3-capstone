"""thrianka naidoo
ndxthr005
assignment6, question4: program to sort marks and create diagram"""

marks = input("Enter a space-separated list of marks:\n")#input from user
marks_list = (marks.split(" "))                          #splits string into a list

count1 =0                                                #initalising counters for each mark
count2 =0
count3 =0
count4 =0
count5 =0

for i in range(len(marks_list)):                        #iterates for each mark
    value = int(marks_list[i])
    if value>=75:                                       #paths for catergories
        count1+=1
    elif 50<=value<60:
        count2+=1
    elif 60<=value<70:
        count3+=1
    elif 70<=value<75:
        count4+=1
    elif value<50:
        count5+=1    
    
print("1 |","X"*count1,sep="")                            #output
print("2+|","X"*count4,sep="")
print("2-|","X"*count3,sep="")
print("3 |","X"*count2,sep="")
print("F |","X"*count5,sep="")
#print(marks_list)