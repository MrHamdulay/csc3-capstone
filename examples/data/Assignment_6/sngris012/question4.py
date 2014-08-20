#Rishen Singh SNGRIS012
#Question Three Assignment 6
marks = input("Enter a space-separated list of marks:\n") #List of marks
marks2 = marks.split() #removes spaces
listOfMarks = [] #array to store marks

fail = 0
third = 0
secondLow = 0
secondUp = 0
first = 0 

for j in range (len(marks2)): #converts all the marks into integer
    marks2[j] = eval(marks2[j])
    listOfMarks.append(marks2[j])
    
for i in marks2: #sorts the marks into categories and records how many marks fall into each category
    if ( 0 <= i < 50):
        fail+=1
    elif (i< 60):
        third+=1
    elif (i < 70):
        secondLow+=1
    elif (i < 75):
        secondUp+=1
    else:
        first+=1
#Prints out the number of marks that fall into each category.
print("1 |","X"*first,sep='')
print("2+|","X"*secondUp,sep='')
print("2-|","X"*secondLow,sep='')
print("3 |","X"*third,sep='')
print("F |","X"*fail,sep='')
        