""" Question 1: gets students in a file and identifies which need to see an adivsor based on whether their marks are more than 1 std deviation below the mean.
Galya Wolov
11 May 2014"""
#import math so that it can be used for calculations later on
import math 

#asks,open, read and closes inputted file
filename= input("Enter the marks filename:\n")
f = open(filename, 'r')
lines = f.readlines()
f.close()


#this removes the \n from lines
for item in range(len(lines)):
    lines[item]= lines[item][:-1]

#makes a list from lines and then splits it into two lists of just numbers and names

p=",".join(lines)
numandnames=p.split(",")
list_no= []
name=[]
for item in range(len(numandnames)):
    if item%2!=0:
        list_no.append(int(numandnames[item]))
    else:
        name.append(numandnames[item])

#calculates the mean 
def mean(list_no):
    sum=0.0
    for num in list_no:
        sum= sum + num
    meaned= sum/len(list_no)
    return meaned

#calculates the standard deviation 
def stdDev(list_no, meaned):
    dev= 0.0
    for num in list_no:
        dev+= ((num-meaned)**2)
    stdeved = math.sqrt(dev/len(list_no))
    return stdeved

#provides variables to use the above functions in future code
meaned = mean(list_no)
stdeved= stdDev(list_no, meaned)
stdDev(list_no, meaned)

#forms list of names with marks below the mean by 1 std deviation
needadvisor= []
for i in list_no:
    if i < meaned-stdeved:
        needadvisor.append(i)

#prints the average, std dev and names of students who need advisor     
print("The average is:", "{:.2f}".format(meaned)) #formats for 2 decimal places
print("The std deviation is:", "{:.2f}".format(stdeved))

if needadvisor != []:
    print("List of students who need to see an advisor:")
    for i in list_no:
        if i in needadvisor:
            indexed=list_no.index(i)
            print(name[indexed])


         


    
    






    