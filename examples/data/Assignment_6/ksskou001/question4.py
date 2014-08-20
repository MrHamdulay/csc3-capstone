'''This program prints out an histogram representation of 
given marks according to the mark categories at UCT
Kouame Hermann KOUASSI : KSSKOU001
19 april 2014'''

def get_marks():
    '''get and returns the list of marks as a string'''
    marks_str = input('Enter a space-separated list of marks:\n')
    #split the string using spaces to get an array of marks
    marks = marks_str.split(' ')
    #return mark array
    return marks

def counter(list):
    '''returns a dictionary containing the histogram reppresentation
    with an list as parameter'''
    #definiting and initializing of the mark categories
    fail = 0
    third = 0
    lower = 0
    upper = 0
    first = 0
    #iterate over the marks of the list
    for i in list:
        #find the mark category of each mark and increment the category under which it falls
        if eval(i) < 50:
            fail += 1
        elif 50<=eval(i) < 60:
            third += 1
        elif 60 <= eval(i) < 70:
            lower += 1
        elif 70 <= eval(i) < 75:
            upper += 1
        else:
            first += 1
    #creat a dictionary that link each mark category to the height of its histogram 'X' 
    dictionary = {'1 |':'X'*first,'2+|':'X'*upper,'2-|':'X'*lower,'3 |':'X'*third,'F |':'X'*fail}
    return dictionary

def display(dictionary):
    '''function to print the histogram representation'''
    #sorted the mark categories in a descending achievement
    categories = sorted(dictionary)
    #iterate over the categories to print out each category and its representative histogram
    for i in categories:
        print(i, dictionary[i], sep = '')    

def main():
    '''main function'''
    #get marks
    marks = get_marks()
    #match up each category with his representative histograme
    dictionary = counter(marks)
    #print out the histogram
    display(dictionary)
    
    
if __name__=="__main__":
    main()
            
            