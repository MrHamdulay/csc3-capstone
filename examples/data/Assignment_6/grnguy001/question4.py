#Done By Guy Green

#Creating the Mark classes(Group)
markGroup=[0,0,0,0,0]

#Asking for marks from user
marksGiven=input("Enter a space-separated list of marks:\n")

#Seperating marks
marksGiven=marksGiven.split(" ")

#Seperating marks into groups
#Not alllowing marks higher than 100 or lower than 0
for i in marksGiven:
    if eval(i)>=75 and eval(i)<=100:
        markGroup[0]+=1
    elif eval(i)>=70:
        markGroup[1]+=1
    elif eval(i)>=60:
        markGroup[2]+=1
    elif eval(i)>=50:
        markGroup[3]+=1
    elif eval(i)<50 and eval(i)>=0:
        markGroup[4]+=1
    else:
        print("Invalid Mark")

#Printing it
print("1 |"+markGroup[0]*"X")
print("2+|"+markGroup[1]*"X")
print("2-|"+markGroup[2]*"X")
print("3 |"+markGroup[3]*"X")
print("F |"+markGroup[4]*"X")