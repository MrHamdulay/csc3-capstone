#MTHKHI001
#Khiraad Mathura
#Question 4

# get input for list of marks
marks = input("Enter a space-separated list of marks:\n")
marksArray = marks.split(" ")
for i in range (len(marksArray)):
    #convert strings to numbers
    marksArray[i] = eval(marksArray[i])
    
    
# implement counters for each grade achieved    
count_first = 0
count_upper_second = 0
count_lower_second = 0
count_third = 0
count_fail = 0

# loop through array and assign each score to its relevent counter, increase counter by 1 everytime a score meets its criterium
for j in range (len(marksArray)):
    if(marksArray[j] < 50):
        count_fail = count_fail + 1
    if(50 <= marksArray[j] < 60):
        count_third = count_third + 1
    if(60 <= marksArray[j] < 70):
        count_lower_second = count_lower_second + 1    
    if(70 <= marksArray[j] < 75):
        count_upper_second = count_upper_second + 1
    if(75 <= marksArray[j]):
        count_first = count_first + 1

#print histogram, using numbers tallied by counters        
print("1 |" + "X"*count_first)
print("2+|" + "X"*count_upper_second)
print("2-|" + "X"*count_lower_second)
print("3 |" + "X"*count_third)
print("F |" + "X"*count_fail)