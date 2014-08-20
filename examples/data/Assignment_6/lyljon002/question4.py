#20 April 2014  
#Assignment 6, Question 4, create a histogram of marks
#LYLJON002


symbollist = ["1 ", "2+", "2-", "3 ", "F "]    #symbols for various marks
gradeslist = [101, 75, 70, 60, 50,0] #upper and lower limits for marks

string = ""

markslist = input("Enter a space-separated list of marks:\n").split(" ") #receive all marks

for z in range(1,6):    #loop
    string= "|"
    for y in markslist:     #run through marks
        if (int(y) >= gradeslist[z]) and (int(y) < gradeslist[z-1]): #check lower and upper limits
            string = string + "X"                   #build string
    print(symbollist[z-1] + string)             #output symbol + built string