# assignment 6 question 4
marks = input("Enter a space-separated list of marks:\n").split()
for i in range(len(marks)):
    marks[i] = eval(marks[i])
results = [["1 |",0],["2+|",0],["2-|",0],["3 |",0],["F |",0]]
for i in range(len(marks)):
    if marks[i] >= 75:
        results[0][1] += 1
        continue
    if marks[i] >= 70:
        results[1][1] += 1  
        continue
    if marks[i] >= 60:
        results[2][1] += 1   
        continue
    if marks[i] >= 50:
        results[3][1] += 1
        continue
    results[4][1] += 1 
for i in range(len(results)):
    print(results[i][0], "X" * results[i][1], sep = "")
#print("1 |", end = "")
#mark = 100
#index = 0

#while mark >= 75:
    #mark = marks[index]
    #if mark < 75:
        #break
    #print("X", end ="")
    #index += 1


#print("\n2+|", end = "")
#while mark >= 70:
    #mark = marks[index]
    #if mark < 70:
        #break
    #print("X", end ="")
    #index += 1

#print("\n2-|", end = "")
#while mark >= 60:
    #mark = marks[index]
    #if mark < 60:
        #break
    #print("X", end ="")
    #index += 1
    
#print("\n3 |", end = "")
#while mark >= 50:
    #mark = marks[index]
    #if mark < 50:
        #break
    #print("X", end ="")
    #index += 1    

#print("\nF |", "X" * (len(marks) - index), sep = "")