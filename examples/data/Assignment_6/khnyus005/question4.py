'''
Created on 22 Apr 2014
histogram of symbols of marks
@author: Yusuf Khan
KHNYUS005
'''

marks = (input('Enter a space-separated list of marks:\n')).split()
# input string and create array of data
histo = [0,0,0,0,0]#initializing array

for i in range(len(marks)):#loop through array
    marks[i] = eval(marks[i])#counting each symbol in array
    if marks[i] < 50:
        histo[0] += 1
    elif marks[i] < 60:
        histo[1] += 1
    elif marks[i] < 70:
        histo[2] += 1
    elif marks[i] < 75:
        histo[3] += 1
    else:
        histo[4] +=1
        
#output histogram
print ('1 |'+('X'*histo[4]))
print ('2+|'+('X'*histo[3]))
print ('2-|'+('X'*histo[2]))
print ('3 |'+('X'*histo[1]))
print ('F |'+('X'*histo[0]))