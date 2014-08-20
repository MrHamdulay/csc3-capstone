""" student average marks
alexander whiting
11 may 2014"""
keys = []
def create(data,file):
    wholesent = file.readlines()
    global keys
    for i in wholesent:
        sent = i.rstrip('\n').split(',')
        data[sent[0]] = eval(sent[1])
        keys.append(sent[0])

def average(data):
    tot = 0
    
    for i in data:
        tot += data[i]
    ave = tot/len(data)
    return ave

def sd(ave,data):
    tot = 0 
    for i in data:
        tot += (data[i] - ave)**2
    sd = (tot/len(data))**0.5
    return sd
     


def needAD(ave,sd,data):
    count = 0
    for i in keys:
        if ave-data[i]>sd:
            count += 1
            if count ==1:
                print("List of students who need to see an advisor:")
            print(i)


filename = input("Enter the marks filename:\n")
marksfile = open(filename, 'r')
marks = {}
create(marks,marksfile)
marksfile.close()
ave = average(marks)
std = sd(ave,marks)
print("The average is: "+"{0:.2f}".format(ave))
print("The std deviation is: "+"{0:.2f}".format(std))

needAD(ave,std,marks)



