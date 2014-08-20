'''Question 1 Assignment 9
Charlie Shang
SHNHUA002
2014.05.15'''

infile = open(input("Enter the marks filename:\n"), "r")

lines = infile.readlines() #read file lines into a list
infile.close()

numlist = [] #list for individual marks

std = 0
mean = 0


for name in lines: # deletes the last character in every name
    name = name[:-1] 

for i in range(len(lines)): 
    mark = int(lines[i][lines[i].find(',')+1::]) #find the mark, which is after the first comma
    mean += mark
    numlist.append(mark) #add mark to list
    
mean = mean/len(lines)

print("The average is: " + "%0.2f"%(mean)) #fixed to 2 decimals

for mark in numlist:
    std += ((mark-mean)**2) 

std = (std/len(numlist))**(1/2)

print("The std deviation is: " + "%0.2f"%(std))

listfailure= [] #people who need to see student advisor

for i in range(len(lines)): 
    if numlist[i] < (mean-std):
        listfailure.append(lines[i][0:lines[i].find(',')]) #add name to listfailure if mark is too low
        
if len(listfailure) > 0: #if there are people in the list
    print("List of students who need to see an advisor:")
    for name in listfailure:
        print(name)