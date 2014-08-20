"""Output histogram  of mark categories at UCT
Ross Eyre
20/04/2014"""

#create lists of marks + counter dictionary
marks = input("Enter a space-separated list of marks:\n").split(" ")
counters = {'1':0, '2+':0 , '2-':0 , '3':0 , 'F': 0}

#count and populate counter dictionary according to tiers
for i in range (len(marks)):
    if eval(marks[i]) >= 75:
        counters['1'] += 1
    elif eval(marks[i]) >= 70:
        counters['2+'] += 1
    elif eval(marks[i]) >= 60:
        counters['2-'] += 1
    elif eval(marks[i]) >= 50:
        counters['3'] += 1
    else:
        counters['F'] += 1
        
#print histogram

print ("1 |" + "X"*counters['1'])
print ("2+|" + "X"*counters['2+'])
print ("2-|" + "X"*counters['2-'])
print ("3 |" + "X"*counters['3'])
print ("F |" + "X"*counters['F'])