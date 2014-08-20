'''program to determine which students need to see a student advisor
tom new
2014/05/10'''

def getmarks (filename):
    '''extracts student names and marks from a text file into a 2D list'''
    
    # extracts the lines as strings into the marklist variable
    source = open (filename, 'r')
    marklist = []
    
    for line in source:
        if line [-1:] == '\n': # strips new lines
            line = line [:-1]
        line = line.split (',') # splits into list of student name and mark
        line [1] = float (line [1]) # turns the mark into a number
        marklist.append (line) # sends line to new element in marklist
        
    source.close ( )
    
    return marklist

def mean (l):
    '''returns the arithmetic mean of its arguments'''
    try:
        
        # self-explanatory
        mean = 0
        for x in l:
            mean += x
        mean /= len (l)
        
    # handles empty lists
    except ZeroDivisionError:
        mean = 'Division by zero error! Was the list empty?'
        
    # handles lists of strings
    except TypeError:
        mean = 'You didn\'t enter a list, or the elements of the list you entered weren\'t numbers!'
    finally:
        return mean
    
def sigma (l):
    '''returns the standard deviation of its arguments'''
    
    import math # for math.sqrt ( )
    mew = mean (l)
    N = len (l)
    var = 0
    
    # iterates through numbers in the list
    for x in l:
        var += (x - mew)**2
    sigma = var/N
    return math.sqrt (sigma)

def sendtoadv (l):
    '''returns list of students 1 std deviation below the mean'''
    
    x = [] # list of students to be sent to student advisor
    marks = []
    
    # sends a list of each student's mark to marks
    for i in range (len (l)):
        marks.append (l [i][1])    
    
    sd, average = sigma (marks), mean (marks)
    
    # compares each student in l with sigma, if lower by one sigma, sends to x
    for student in l:
        if student [1] < average - sd:
            x.append (student [0])
    return x

if __name__ == '__main__':
    filename = input ('Enter the marks filename:\n')
    marklist = getmarks (filename)
    marks = []
    
    # calulates mean and sd for user's list
    for i in range (len (marklist)):
        marks.append (marklist [i][1])
    print ('The average is: {:.2f}'.format (mean (marks)))
    print ('The std deviation is: {:.2f}'.format (sigma (marks)))
    advlist = sendtoadv (marklist)
    
    # checks if there are students who need to see the advisor
    if advlist != []:
        print ('List of students who need to see an advisor:')
        for i in advlist:
            print (i)