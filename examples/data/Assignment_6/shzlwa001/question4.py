# Pragram for drawing a histogram for marks
# Lwazi Shezi
# 25 April 2014


# get marks
mark_list = input('Enter a space-separated list of marks:\n')
 
# make a list from marks
marks = mark_list.split()

# initialise grade variables
firsts = 0
upper_seconds = 0
lower_seconds = 0
thirds = 0
fails = 0

# get the number of each grades or mark ranges
for i in marks:
    i = eval(i)
    if i >= 75:
        firsts = firsts + 1
    elif 70 <= i < 75:
        upper_seconds += 1
    elif 60 <= i < 70:
        lower_seconds += 1
    elif 50 <= i < 60:
        thirds += 1
    else :
        fails += 1
        
# output the histogram for each mark range
print('1 |'+'X'*firsts)
print('2+|'+'X'*upper_seconds)
print('2-|'+'X'*lower_seconds)
print('3 |'+'X'*thirds)
print('F |'+'X'*fails)