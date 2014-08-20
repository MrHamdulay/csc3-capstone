"""program to draw histogram of marks
Tim Hardie
23-4-14"""

if __name__ == '__main__':
    #input marks and convert to ints
    mark_list = input ("Enter a space-separated list of marks:\n").split(' ')
    for i in range (len (mark_list)):
        mark_list[i] = eval (mark_list[i])
    
    #categorise marks
    firsts, upper_seconds, lower_seconds, thirds, fails = 0,0,0,0,0
    for mark in mark_list:
        if mark < 50: fails += 1
        elif mark < 60: thirds += 1
        elif mark < 70: lower_seconds += 1
        elif mark < 75: upper_seconds += 1
        else: firsts += 1
    
    #draw histogram
    print ("1 ", 'X'*firsts, sep='|')
    print ("2+", 'X'*upper_seconds, sep='|')
    print ("2-", 'X'*lower_seconds, sep='|')
    print ("3 ", 'X'*thirds, sep='|')
    print ("F ", 'X'*fails, sep='|')