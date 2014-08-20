#Assignment 6
#Question 4
#Barry Su
#23 April 2014
#Program that draws a historgram with a list of marks according to UCT mark catergories


#get the list of marks
marks = input("Enter a space-separated list of marks: \n")

#split the numbers so they are a list
marks = marks.split()

#create a counter for each category
fail = 0
third = 0
lo_sec = 0 
up_sec = 0
first = 0

#evaluate the marks
for i in range(len(marks)):
    marks[i] = eval(marks[i])

#run through each mark and put it in the corresponding category
for i in marks:
    if i < 50:
        fail += 1
    elif 50 <= i < 60:   
        third += 1
    elif 60 <= i < 70:
        lo_sec += 1 
    elif 70 <= i < 75:
        up_sec += 1
    else:
        first += 1
            
#print out vote counts for each party
print ("1 ", "|", "X"*first, sep="")
print ("2+", "|", "X"*up_sec, sep="")
print ("2-", "|", "X"*lo_sec, sep="")
print ("3 ", "|", "X"*third, sep="")
print ("F ", "|", "X"*fail, sep="")