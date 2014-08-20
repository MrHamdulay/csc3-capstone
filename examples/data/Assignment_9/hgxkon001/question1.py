#Konrad Hugo
#Assignment 9 question 1
import math
filename = input('Enter the marks filename:\n') #The user's inputed filename


def averager(content): #Function calculating the mean
	
	summed = 0
	for i in content:
		summed += i
	return (summed/len(content))

def standarder(content): #Function calculating standard deviation
	
	summed = 0 #variable acting as part of std deviation calcuation
	avg = averager(content)
	for i in content:
		summed += (i-avg)*(i-avg)
	return math.sqrt(summed/len(content))


file = open(filename,"r");

file_list = file.readlines();

file.close()



pupil_names = [] #blank lists to save ouoil names and marks separately 
pupil_marks = []


for line in file_list: #Takes each list(line) in the list of lines(also list form)
	
	pupil_names.append(line.split(",")[0]) #This adds only names to one list by isolating the names due to their positions(name,mark) (i.split(',') is a list here 
	pupil_marks.append(int(line.split(",")[1].replace('\n',''))) #Adds marks to list by isolating position & makes it integer. swaps \n with ''. i


mean = averager(pupil_marks)
standard_dev = standarder(pupil_marks) #These two variables call the function to be used and to use the returned value

print('The average is: %0.2F' %mean) #Formatting

print('The std deviation is: %0.2F' %standard_dev) #Formatting

advisee = 'List of students who need to see an advisor:'


for i in range(len(pupil_marks)): 
	
	if pupil_marks[i]<(mean - standard_dev): #Finds the marks that are inadequate and as the number of marks = number of pupils in each list, i is position of the linked mark and name
		advisee += '\n' + pupil_names[i]

if advisee != 'List of students who need to see an advisor:': #This prevents that line being printed if there arent any students who qualify for a advisor
	print(advisee)