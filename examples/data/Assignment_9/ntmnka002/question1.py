infn = input('Enter the marks filename:\n')

n = []
m = []

infn = open(infn, 'r')
pos = 0

#===============================================================
#Writing to the arrays
for k in infn:
    for i in range(len(k)):
        
        if k[i] == ',':
            pos = i
    
    name = k[:pos]
    
    mark = k[pos + 1:]
    
    n.append(name)
    m.append(mark)

#===================================================================
#Calc ave and sdev
total = 0

for k in range(len(m)):
    total += int(m[k])
    
ave = total / len(m) #have to format it (2dec)


#Calulate sdev
sdave = 0
sdtot = 0

for k in range(len(m)):
    sdtot += int(m[k])
    
sdave = sdtot / len(m)

sdsqmean = 0

import math

for k in range(len(m)):
    sdsqmean = sdsqmean + ((int(m[k]) - sdave) ** 2)    

sdsqmean = sdsqmean / len(m)

sdsqmean = math.sqrt(sdsqmean)

compare = ave - sdsqmean
    
#=========================================================
#output
ave = '{0:.2f}'.format(ave)
nsdsqmean = '{0:.2f}'.format(sdsqmean)

print('The average is:', ave)
print('The std deviation is:', nsdsqmean)

if (sdsqmean) > 0:
    
    print('List of students who need to see an advisor:')
    
    for k in range(len(m)):
        if int(m[k]) < compare:
            print(n[k])