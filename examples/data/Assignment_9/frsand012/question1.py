import math

marks = input("Enter the marks filename:\n")

def deviation():
    f = open(marks, "r")
    lines = f.readlines()
    f.close
        
    pairs = [[""]] * len(lines)
    for j in range(len(lines)):
        pairs[j] = lines[j].split(",")
    
    total = 0
    counter = 0
    for k in range(0,len(pairs)):
        total += eval(pairs[k][1])
        counter += 1
    average = total/counter
    
    std_deviation = 0
    for l in range(len(pairs)):
        std_deviation += (eval(pairs[l][1]) - average)**2
    std_deviation = math.sqrt(std_deviation/counter)  
    
    advice = []
    for m in range(len(pairs)):
        if average - std_deviation > eval(pairs[m][1]):
            advice.append(pairs[m][0])
        
    print("The average is:", "%.2f" % average) 
    print("The std deviation is:", "%.2f" %std_deviation)
    if advice != []:
        print("List of students who need to see an advisor:")
        for l in advice:
            print(l)     

deviation()