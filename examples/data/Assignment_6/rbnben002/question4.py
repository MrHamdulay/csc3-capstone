X = []
mark = input("Enter a space-separated list of marks:\n")
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
X = mark.split(" ")
for i in range (len(X)):
    if eval(X[i]) >= 75:
        count1 = count1 + 1
    elif eval(X[i]) < 75 and eval(X[i]) >= 70:
        count3 = count3 + 1
    elif eval(X[i]) < 70 and eval(X[i]) >= 60:
            count2 = count2 + 1
    elif eval(X[i]) < 60 and eval(X[i]) >= 50:
                count4 = count4 + 1 
    elif eval(X[i]) <50:
        count5 = count5 + 1
print ("1 |",count1*"X",sep="")
print ("2+|",count3*"X",sep="")
print ("2-|",count2*"X",sep="")
print ("3 |",count4*"X",sep="")
print ("F |",count5*"X",sep="")