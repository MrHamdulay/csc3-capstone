#create a histogram from a list of marks
#annika brundyn
#24/04/2014

#ask for input from user and create list
marks=input("Enter a space-separated list of marks:\n")
marks=marks.split()
marks=[int(i) for i in marks]           #convert input to integers

#create dictionary and classify marks
marks_count={"F":0,"3":0,"2-":0,"2+":0,"1":0}   #create dictionary with empty values
for i in marks:
    if i<50: 
        marks_count["F"]+=1
    if 50<=i<60:
        marks_count["3"]+=1
    if 60<=i<70:
        marks_count["2-"]+=1
    if 70<=i<75:
        marks_count["2+"]+=1
    elif i>=75:
        marks_count["1"]+=1

#print histogram:
print("1 |","X"*marks_count["1"],sep="")
print("2+|","X"*marks_count["2+"],sep="")
print("2-|","X"*marks_count["2-"],sep="")
print("3 |","X"*marks_count["3"],sep="")
print("F |","X"*marks_count["F"],sep="")