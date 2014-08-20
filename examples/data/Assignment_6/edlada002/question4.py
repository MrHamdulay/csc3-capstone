"""marks histogram printer"""


marks = []

marks = input("Enter a space-separated list of marks:\n").split(" ")


first = 0
uSecond = 0
lSecond =0
third =0
fail = 0


for i in range(len(marks)):
    
    marks[i] = int(marks[i])
    

    if (marks[i] >= 75):
        first +=1
        
    elif (70<= marks[i] <75 ):
        uSecond+=1
        
    elif ( 60<= marks[i]<70):
        lSecond +=1
        
    elif (50 <=marks[i] <60):
        third+=1
        
    elif ( marks[i]<50):
        fail+=1
        
print("1 |",first*"X",sep ="")
print("2+|",uSecond*"X",sep ="")
print("2-|",lSecond*"X",sep ="")
print("3 |",third*"X",sep ="")
print("F |",fail*"X",sep ="")

        
    
    