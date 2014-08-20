"""nasha somoina meoli
24th april 2014
program to classify grades and draw a histogram."""

def marks():
    #to get list of marks
    x = input("Enter a space-separated list of marks:\n")
    listofmarks = x.split(" ")
    finallist=[]
    for i in listofmarks:
        mark1 = eval(i)
        finallist.append(mark1)    
    # to keep track of grades in each category
    counter = {"fail":0, "third": 0 ,"lowersecond":0, "uppersecond":0,"first":0}
    #to classify marks
    for mark in finallist:
        if (mark>=75):
            counter["first"]+=1
        elif (mark>=70):
            counter["uppersecond"]+=1
        elif (mark >= 60):
            counter["lowersecond"]+=1
        elif (mark >= 50):
            counter["third"]+=1
        else:
            counter["fail"]+=1
    #to print histogram
    print("1 |"+"X"*counter["first"])
    print("2+|"+"X"*counter["uppersecond"])
    print("2-|"+"X"*counter["lowersecond"])
    print("3 |"+"X"*counter["third"])
    print("F |"+"X"*counter["fail"])
        
marks()
    