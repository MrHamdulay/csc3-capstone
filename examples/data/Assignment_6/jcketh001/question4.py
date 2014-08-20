#Program that makes a histogram of marks entered by the user
#Ethan Jackson          
#24 April 2014

#lets user enter several numbers whereby each number is added to a list
enter = input("Enter a space-separated list of marks:\n").split()
counters = [0, 0, 0, 0, 0]#empty list of number of each category of mark
for i in enter:
    if eval(i) >=75:#Parameters for each category
        counters[0] += 1#adds a count to the list if in the respective category
    elif 75 > eval(i) >= 70:
        counters[1] += 1
    elif 70 > eval(i) >= 60:
        counters[2] += 1
    elif 60 > eval(i) >= 50:
        counters[3] += 1
    else:
        counters[4] +=1
        
print("1","|"+"X"*counters[0]) #print the axes with the counts of each category of mark
print("2+"+"|"+"X"*counters[1])
print("2-"+"|"+"X"*counters[2])
print("3","|"+"X"*counters[3])
print("F","|"+"X"*counters[4])
            