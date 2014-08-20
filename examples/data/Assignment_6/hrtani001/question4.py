#Output histogram representation
#Aniq Hartle
#25/04/2014

#take input and split into array
marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(" ")

#initialise variables
first = 0
l_second = 0
u_second = 0
third = 0
fail = 0

#check category of array contents and tally
for i in marks:
    if eval(i)<50:
        fail+=1
    elif eval(i)<60:
        third+=1
    elif eval(i)<70:
        l_second+=1
    elif eval(i)<75:
        u_second+=1
    elif eval(i)>=75:
        first+=1

#print output with X*theTallyNumber        
print("1 |","X"*first,sep="")
print("2+|","X"*u_second,sep="")
print("2-|","X"*l_second,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")