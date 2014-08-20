

filename= input("Enter the marks filename:\n")
#open file
f = open(filename,"r")
lines = f.readlines()
f.close()
newlist =[]
for i in range (len(lines)):
    newlist.append(lines[i].replace('\n','').split(","))

sum = 0
for i in range(len(newlist)):
    sum += eval(newlist[i][1])

n = len(newlist)
mean = sum/n

count = 0
for i in range(len(newlist)):
    count = count + (eval(newlist[i][1])-mean)**2

std = ((count)/n)**(0.5)
   
print("The average is: {:.2f}".format(mean))
print("The std deviation is: {:.2f}".format(std))
bool = True
for i in range(len(newlist)):
    if eval(newlist[i][1])<(mean-std):
        if bool:
            print("List of students who need to see an advisor:")
            bool = False 
        print(newlist[i][0])