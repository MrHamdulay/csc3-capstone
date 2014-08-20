#Darryl Gounden
#10/05/14
#Checks for students with a mark below one standard deviation form the mean

import math

filename = input("Enter the marks filename:\n")

#Opens the file and creates a list of each line
f = open(filename,"r")
doc=f.readlines()
f.close()

#Seperates the text file into useful lists and deletes waste characters
total = len(doc)
for i in range(total):
    if doc[i][-1] == "\n":
        doc[i] = doc[i][:-1]
for i in range(total):
    doc[i] = doc[i].split(",")
    
#Finds the average    
summ = 0   
for i in range(total):
    summ += eval(doc[i][1])    
formA = "The average is: {0}.{1:0<2}"
average = str(round(summ/total,2))
av_string = average.split(".")
print(formA.format(av_string[0],av_string[1]))

#Finds the sd
sd_part1 = 0
for i in range(total):
    sd_part1 += ((eval(doc[i][1]) - eval(average)) ** 2)
sd = str(round(math.sqrt(sd_part1/total),2))
listing_sd = sd.split(".")
formSD = "The std deviation is: {0}.{1:0<2}"
print(formSD.format(listing_sd[0],listing_sd[1]))

#Finds cutoff and prints names of students below the cutoff
cutoff= eval(average) - eval(sd)
listing=[]
for i in range(total):
    if eval(doc[i][1]) < cutoff:
        listing.append(doc[i][0])
        
if len(listing)>0:
    print("List of students who need to see an advisor:")
    for i in range(len(listing)):
        print(listing[i])
    
        

      
      

