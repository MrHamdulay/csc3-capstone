# Grade Histogram drawer
# Mutali Mashamba
# 22 April 2014

def histo_thinga():
    # Prompt user to enter marks
    grades = input('Enter a space-separated list of marks:\n')
    # Turn the string into a list
    grade_list = grades.split(' ')
    # counters for all grades set to zero
    f = 0
    th = 0
    up = 0
    lo = 0
    fst = 0
    # counting the numbers of the differnet grades
    for mark in grade_list:
        mark = eval(mark)
        if 0 <= mark < 50:
            f += 1
        elif 50 <= mark < 60:
            th += 1
        elif 60 <= mark < 70:
            lo += 1
        elif 70 <= mark < 75:
            up += 1
        elif 75 <= mark <= 100:
            fst += 1
        else:
            break
    # Print the histogram (multiply the character "X" by the count of the grade)
    print('1 |'+'X'*fst)
    print('2+|'+'X'*up)
    print('2-|'+'X'*lo)
    print('3 |'+'X'*th)
    print('F |'+'X'*f)
    # Be Happy
histo_thinga()
            