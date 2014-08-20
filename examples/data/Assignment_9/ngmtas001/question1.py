#Tase Ngambi
#13/05/2014
#Question1

 
#recieve the filename    
filename = input("Enter the marks filename:\n")

try:
    Testfile = open(filename)
    
    line = Testfile.readlines()
    names = []
    marks = []
    #inputting the testfile contents into 2 arrays
    for x in line:
        parts = x.split(",")
        names.append(parts[0])
        marks.append((parts[1])[0:2])
       
    #working out the average        
    total = 0       
    for x in marks:
        total = total + int(x)
    average = round(total/len(marks),2)
    
    #working out the standard deviation
    total2 =0
    for x in marks:
        total2 = total2+ (int(x) -average)**2
    stdv = round((total2/len(marks))**0.5,2)
    
    #placing numbers as strings
    newaverage = str(average)
    newstdv = str(stdv)
    
    if str(average)[-1] =="0":
        newaverage = str(average)+"0"
    
    if str(stdv)[-1] =="0":
        newstdv = str(stdv)+"0"  
        
   
    print("The average is: ",newaverage, sep ="")
    print("The std deviation is: ",newstdv, sep ="")
    
    #checking to see if the mark is less than one stdv from mean
    if len(marks) != 1:
        print("List of students who need to see an advisor:")
        for x in range (len(marks)):
            if int(marks[x]) <= (average-stdv):
                print(names[x])
except:
    print()
    



    
    