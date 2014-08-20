
marks = (input ("Enter a space-separated list of marks:\n"))
#create the array to hold marks and dictionary to hold the total of each mark tyope
list = []
histogramMarks ={"first":0,"upperSecond":0,"lowerSecond":0,"third":0,'fail':0}

list = (marks).split(" ")
x=0
#check which category marks fall into and add one to the corresponding mark in dictionary
for i in list:
    if(list[x]=="100"):
        histogramMarks["first"] +=1
    elif("75"<=list[x]):
        histogramMarks["first"] +=1
            
    elif("50"<=list[x]<"60"):
        histogramMarks["third"] +=1
    elif("60"<=list[x]<"70"):
        histogramMarks["lowerSecond"] +=1
    elif("70"<=list[x]<"75"):
        histogramMarks["upperSecond"] +=1
    
    elif(list[x]<"50"):
        histogramMarks["fail"] +=1    
    x+=1
    
#print the histogram
print("1 |","X"*histogramMarks["first"],sep="")
print("2+|","X"*histogramMarks["upperSecond"],sep="")
print("2-|","X"*histogramMarks["lowerSecond"],sep="")
print("3 |","X"*histogramMarks["third"],sep="")
print("F |","X"*histogramMarks["fail"],sep="")

           
        

    