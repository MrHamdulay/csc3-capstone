"""Keegan Naidoo
NDXKEE009
21 April 2014"""

marks=[]       #Creates empty list for marks
counter=[]     #Creates empty list to count how many marks are in each category

count=0
index=0
b=0

marks=input("Enter a space-separated list of marks:\n").split(" ") #Inputs marks


for i in range(len(marks)):    #Runs through list of marks
   
    #print (marks[i])
    
    int_marks=int(marks[i])    #Converts marks to integers
    
    if int_marks>=75:          #Counts how many marks are in the 75 category  
        count+=1         
    counter.insert(i,count)     #Inserts marks into list at position i
    index+=1                    #Adds 1 to the index each time

Number_of_people=counter[index-1]         #Variable to keep track of how many people are in the category

count=0           #Re-assigns count to 0.Deletes old data stored in count
index=0           #Re-assigns index to 0.Deletes old data stored in index

#From here on the code is the same for the different categories. It is just adjusted to fit into the different categories

print("1 |","X"*Number_of_people,sep='')

for i in range(len(marks)):
    
    int_marks=int(marks[i])
    
    if int_marks>=70 and int_marks<75:
        count+=1
    counter.insert(i,count)
    index+=1
Number_of_people=counter[index-1]

print("2+|","X"*Number_of_people,sep='')

count=0
index=0

for i in range(len(marks)):
    
    int_marks=int(marks[i])
    
    if int_marks>=60 and int_marks<70:
        count+=1
    counter.insert(i,count)
    index+=1
Number_of_people=counter[index-1]

print("2-|","X"*Number_of_people,sep='')

count=0
index=0

for i in range(len(marks)):
    
    int_marks=int(marks[i])
    
    if int_marks>=50 and int_marks<60:
        count+=1
    counter.insert(i,count)
    index+=1
Number_of_people=counter[index-1]

print("3 |","X"*Number_of_people,sep='')

count=0
index=0

for i in range(len(marks)):
    
    int_marks=int(marks[i])
    
    if int_marks<50:
        count+=1
    counter.insert(i,count)
    index+=1
Number_of_people=counter[index-1]

print("F |","X"*Number_of_people,sep='')