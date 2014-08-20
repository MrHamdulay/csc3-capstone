#Assignment 6 Question 4
#Carissa Moodley
#Histogram representation of a list of marks

print("Enter a space-separated list of marks:")
marks=input() #allows user to input a list of marks
marks=marks.split(" ") #converting the marks inputed by the user into a list



for i in range(0,len(marks),1):
    marks[i]=int(marks[i]) #converting each item in the list into an integer
count = [0,0,0,0,0]  #list created to count for each mark category 

for i in range(0,len(marks),1): #looping throught each mark in the list
    if marks[i]<50:  #for fail
        count[0]+=1
    elif marks[i]<60: #for third
        count[1]+=1
    elif marks[i]<70: #for lower second
        count[2]+=1
    elif marks[i]<75: #for upper second
        count[3]+=1
    else:             #for first
        count[4]+=1    

#displaying in histogram form    
print("1 |"+"X"*count[4]) 
print("2+|"+"X"*count[3])
print("2-|"+'X'*count[2])
print("3 |"+'X'*count[1])
print("F |"+'X'*count[0])