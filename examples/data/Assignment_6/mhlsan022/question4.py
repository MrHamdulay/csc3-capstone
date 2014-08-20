'''A program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
Sandile Christopher Mahlangu
21 April 2014'''

def mark_histogram():
    '''This functions draws a histogram with supplied marks'''
    
    #Getting marks from the user then making a list
    mark_entry=input('Enter a space-separated list of marks:\n')
    marks=mark_entry.split(' ')
    
    #Seperating the marks in to categories
    
    number_of_1sts=0
    number_of_upper_seconds=0
    number_of_lower_seconds=0
    number_of_3rds=0
    number_of_fais=0
    
    for mark in marks:
        if eval(mark)>=75:
            number_of_1sts+=1
        elif eval(mark)>=70:
            number_of_upper_seconds+=1
        elif eval(mark)>=60:
            number_of_lower_seconds+=1
        elif eval(mark)>=50:
            number_of_3rds+=1
        elif eval(mark)<50:
            number_of_fais+=1
    
    #Printing the Histogram
    print('1 |','X'*(number_of_1sts),sep='')
    print('2+|','X'*(number_of_upper_seconds),sep='')
    print('2-|','X'*(number_of_lower_seconds),sep='')
    print('3 |','X'*(number_of_3rds),sep='')
    print('F |','X'*(number_of_fais),sep='')


mark_histogram()