"""Program that outputs a histogram based on a list of marks received..
Trevor Byaruhanga
21 April 2014"""


#fail < 50%
#50% <= 3rd < 60%
#60% <= lower 2nd < 70%
#70% <= upper 2nd < 75%
#1st >= 75%
request=input('Enter a space-separated list of marks:\n')
percentage = request.split (" ")


#start with zero counters
counter_1 = {}
counter_2 = {}
counter_lower2 = {}
counter_3 = {}
counter_fail = {}
#change the items in the list: percentage to numbers
percentage=[int(i) for i in percentage]
for i in percentage:
# if conditions stating what to add to the counter if a particular mark is received.   
    if i>=75:
        if not i in counter_1:
            counter_1[i] = 1
        else:
            counter_1[i] += 1
    elif i>=70:
            if not i in counter_2:
                counter_2[i] = 1
            else:
                counter_2[i] += 1    
    elif i>=60:
            if not i in counter_lower2:
                counter_lower2[i] = 1
            else:
                counter_lower2[i] += 1      
    elif i>=50:
            if not i in counter_3:
                counter_3[i] = 1
            else:
                counter_3[i] += 1   
    elif i>=0:
            if not i in counter_fail:
                counter_fail[i] = 1
            else:
                counter_fail[i] += 1
                
    else:
        print('Error -ve percentage')

# print out counters and histogram representing the mark allocation.
print ('1 |',end='')
for i in counter_1:
# multiply the number of marks in the category by X.   
    print(int(counter_1[i])*'X',end='')
print('')
print ('2+|',end='')
for i in counter_2:
    print (int(counter_2[i])*'X',end='')
print('')
print ('2-|',end='')
for i in counter_lower2:
    print (int(counter_lower2[i])*'X',end='')  
print('')
print ('3 |',end='')
for i in counter_3:
    print (int(counter_3[i])*'X',end='')   
print('')
print ('F |',end='')
for i in counter_fail:
    print (int(counter_fail[i])*'X',end='')    
