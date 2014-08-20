"""a Python program to analyse student marks read in from a file 
and determine which students need to see a student advisor.
Oh Gee
16 May 2014"""

filename = input("Enter the marks filename:\n")
f = open(filename, "r")
lines = f.readlines()
f.close()


"""Create txt file into proper list"""
for line in (lines):
    line = line.split(",")
    #print(lines)
    
    
for i in range (len(lines)):
    lines[i] = lines[i].split(",")
    #print(lines)
    


"""Find total sum and average"""
total = 0
for i in range (len(lines)):
        total = eval(lines[i][1][0:2]) + total
#print(total)

average = total/len(lines)
#print(average)



"""Calculate Std Deviation"""
tbs = 0
for i in range (len(lines)):
    tbs = (eval(lines[i][1][0:2]) - average)**2 + tbs
    
std = (tbs/len(lines))**(1/2)



print("The average is:","{0:.2f}".format(average) )
print("The std deviation is:","{0:.2f}".format(std))


namecount = 0
for i in range (len(lines)):
    if eval(lines[i][1][0:2]) < (average - std):
        namecount = namecount+1
        
if namecount != 0:
    print("List of students who need to see an advisor:")            

"""Find number of Students that need advisor"""
for i in range (len(lines)):
    if eval(lines[i][1][0:2]) < (average - std):
        print (lines[i][0])
