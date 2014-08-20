#NGMTAS001
#Tase Ngambi
#Question 4
#20 April 2014

stringmarks = input("Enter a space-separated list of marks:\n")
#splitting the marks by space
marks = stringmarks.split(" ")
for k in range(len(marks)):
    marks[k] = int(marks[k])
    
grades = [5]    
    
    
count = [0,0,0,0,0]

#counting the amount of each grade
for x in range(len(marks)):
    if marks[x] >= 75:
        count[0] = count[0]+1
    elif 75>marks[x] >= 70:
        count[1] = count[1]+1
    elif 70>marks[x] >= 60:
        count[2] = count[2]+1       
    elif 60>marks[x] >= 50:
        count[3] = count[3]+1 
    elif marks[x] < 50:
        count[4] = count[4]+1 
                
symbols = ['1','2+','2-','3','F'] 
#printing the histogram
for x in range(len(symbols)):
    print(symbols[x], " "*(2-len(symbols[x])), "|", "X"*count[x], sep="")
