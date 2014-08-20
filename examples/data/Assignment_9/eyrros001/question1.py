"""analyse student marks read in from a file
Ross Eyre
11/05/2014"""
import math
import locale
locale.getpreferredencoding()

#open the file
fname = input("Enter the marks filename:\n")
students = open(fname, 'r')
lines = students.readlines()    

# take off ends
for i in range (len (lines)):
    lines[i] = lines[i][:-1]

#write data to seperate lists
names =[]
marks=[]
for i in lines:
    i=i.split(",")
    names.append(i[0])
    marks.append(i[1])    

def main():       
    #Do printing
    print("The average is: ", "{0:.2f}".format(average()), sep="")
    print("The std deviation is: ", "{0:.2f}".format(standDev()), sep="")
    if(needAdviser()!=''):    
        print("List of students who need to see an advisor:\n" + needAdviser())

#calculate average
def average():
    global marks
    avg = 0
    total=''
    for i in marks:
        if(marks[len(marks)-1]!=i):
            total+= i + "+"
        else:
            total+= i
    avg = eval(total)/(len(marks))        
    return avg
    

#calculate standard deviation
def standDev():
    global marks
    avg = average()
    ans = 0
    for x in marks:
        ans += (eval(x)-avg)**2
        
    ans=ans/(len(marks))
    
    ans=round(math.sqrt(ans),2)
    
    return ans
    
def needAdviser():
    global names
    global marks
    avg = average()
    dev = standDev()
    adv=''
    for m in range(len(marks)):
        if(eval(marks[m])<(avg-dev)):
            adv += names[m] + "\n"
    return adv    
    
main()    