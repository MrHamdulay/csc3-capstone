'''
Created on 11 May 2014
Student marks in file analysis
@author: Yusuf Khan
KHNYUS005
'''
name = input("Enter the marks filename:\n")
f = open(name, 'r')#open text file for reading
l = f.readlines()#read each line to array
marks = []#declare variables outside of loops
ave = 0

for i in l:#iterate through list and extract marks
    if i[-1::]=='\n':
        if i[-3]==',':
            marks.append(int(i[-2]))
        else:
            marks.append(int(i[-3:-1:]))
    else:#for last name in list
        if i[-2]==',':
            marks.append(int(i[-1]))
        else:
            marks.append(int(i[-2::]))

for m in marks:#iterate through array to find average of marks
    ave = ave + m    
ave = ave/(len(l))
ave = "%0.2f" % ave#string formatting of average value to 2dp
print("The average is:",ave)
ave = eval(ave)#convert back to float

stdev=0#declared outisde of loop
for x in marks:#loop through and do first part of calculation
    stdev=stdev+((x-ave)**2)
stdev = "%0.2f" % ((stdev/len(l))**0.5)#formatting and rest of st deviation calculation
print('The std deviation is:',stdev)
stdev = eval(stdev)#output and conversion back to float

idiots = []
dp = ave-stdev#"pass" mark
for c in range(len(l)):
    if marks[c]<dp:
        idiots.append(l[c])#adds name to list
if len(idiots)>0:
    print("List of students who need to see an advisor:")
for fails in idiots:
    if fails[-1::]=='\n':
        if i[-3]==',':#if single digit mark
            print(fails[0:-3:])#output names and not marks or commas
        else:
            print(fails[0:-4:])#output names and not marks or commas
    else:
        if i[-2]==',':#if single digit mark
            print(fails[0:-2:])#output names and not marks or commas
        else:
            print(fails[0:-3:])#output names and not marks or commas

f.close()#close file after reading