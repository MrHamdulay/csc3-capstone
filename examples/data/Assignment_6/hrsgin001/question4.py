#Gina Horscroft
#Assignment6

marks = input("Enter a space-separated list of marks:\n")
markA = marks.split(" ")
newmark = []
#counter for the number of marks - corresponds to [F, 3, 2-, 2+, 1]
arrCount = [0,0,0,0,0]

for i in range (len(markA)):
    #converts strings in array to integers in new array
    newmark.append(int(markA[i]))
    #assign mark category (assumes all between 0 and 100)
    #if true, then adds 1 to the counter for that mark
    if (newmark[i] < 50):
        arrCount[0]+=1
    elif (newmark[i]<60):
        arrCount[1]+=1
    elif(newmark[i] < 70):
        arrCount[2]+=1
    elif(newmark[i] < 75):
        arrCount[3]+=1
    else:
        arrCount[4]+=1
#prints histogram        
print("1 |", "X"*arrCount[4], sep = "")
print("2+|", "X"*arrCount[3], sep = "")
print("2-|", "X"*arrCount[2], sep = "")
print("3 |", "X"*arrCount[1], sep = "")
print("F |", "X"*arrCount[0], sep = "")