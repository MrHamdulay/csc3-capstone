# A program that analyses marks read in from a file
# Martin Batek
# 11 May 2014

import math # For sqrt function 
filename = input("Enter the marks filename:\n") # Ask for filename

f = open(filename,"r") # Open file for reading
lines = f.readlines() # Create a variable containing the lines of the file as an array
f.close() # Close file

for i in range(len(lines)):
    if lines[i][-1]=="\n":
        lines[i] = lines[i][:-1] # Remove the \n from the end of each line
   
for i in range(len(lines)):
    lines[i] = lines[i].split(",") # Split each line into name and mark
  
totalmarks = 0 
for i in range(len(lines)):
    totalmarks += eval(lines[i][1]) # Calculate the accumalation of marks achieved by the class
    
average = totalmarks/len(lines) # calculate average of the class

print("The average is:", "{:.2f}".format(average)) # This formatting is necessary so as to ensure that 2 decimal places are printed out (even if they are .00)

sum_of_squares = 0
for i in range(len(lines)):
    sum_of_squares+= (eval(lines[i][1])-average)**2   
std_dev = math.sqrt(sum_of_squares/len(lines)) # Calculate standard deviation

print("The std deviation is:", "{:.2f}".format(std_dev))
for i in range(len(lines)):
    if eval(lines[i][1]) < average - std_dev:
        lowmark = True
        break
    lowmark = False
if lowmark:
    print("List of students who need to see an advisor:") 
for i in range(len(lines)):
    if eval(lines[i][1]) < average - std_dev:
        print(lines[i][0]) # Print out the names of any students whose mark is less than one standard deviation below the mean.

    