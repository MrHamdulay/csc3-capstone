"""The program that represent the marks according to the categories at UCT
Bruce Sontshoto
25 April 2014"""

#creating a list of marks separated by a space

score = []
marks = input("Enter a space-separated list of marks:\n")
mark = marks.split(" ")
for j in mark:
    score.append(eval(j))   #changing the strings in the list into numbers

#counting the numbers in each category
Fail = 0
Third = 0
Lower2nd = 0
Upper2nd = 0
First = 0
for i in range(len(score)):
    if score[i] < 50:
        y = score.count(score[i])
        Fail+=1
        
    elif 50<= score[i] <60:
        y = score.count(score[i])
        Third+=1        
        
    elif 60<=score[i] <70:
        y = score.count(score[i])
        Lower2nd+=1      
        
    elif 70<= score[i] <75:
        y = score.count(score[i])
        Upper2nd+=1      
        
    else:
        if score[i] >=75:
            y = score.count(score[i])
            First+=1      
        
print("1 ","|",First*"X",sep="")
print("2+","|",Upper2nd*"X",sep="")
print("2-","|",Lower2nd*"X",sep="")
print("3 ","|",Third*"X",sep="")
print("F ","|",Fail*"X",sep="")

