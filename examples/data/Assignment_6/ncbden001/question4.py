#PRogram to create a histogram
#Denzel Ncube
#23April2014

#Getting input
marks = input("Enter a space-separated list of marks:\n")
#Splitting the marks into a list
markslst = marks.split(" ")
#Setting all the counters to zero
fail = 0
third = 0
lsecond = 0
usecond = 0
first = 0

#Looping through the list and incrementing counters for correct grade
for i in range(len(markslst)):
    if 0 <= int(markslst[i]) < 50:
        fail += 1
    elif 50 <= int(markslst[i]) < 60:
        third += 1
    elif 60 <= int(markslst[i]) < 70:
        lsecond += 1
    elif 70 <= int(markslst[i]) < 75:
        usecond += 1
    elif 75 <= int(markslst[i]) <= 100:
        first += 1        

#Displaying histogram        
print("1 |" + first * "X")
print("2+|" + usecond * "X")
print("2-|" + lsecond * "X")
print("3 |" + third * "X")
print("F |" + fail * "X")

