'''Program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks 
Daniel M. Tamale
2014-04-22'''

def histogram():
    '''To enter marks and stored as a string'''
    score=[]
    history=[]
    scores=input('Enter a space-separated list of marks:\n')
    score.append(scores)
    score.sort()
    history=scores.split(' ')
    
    '''To print the respective histogram bar for each class according to marks'''
    class_one=0
    for i in history:
        if i>='75' or i =='100':
            class_one+=1
    print ('1 |','X'*class_one,sep='')
    
    class_two=0
    for i in history:
        if '70'<=i<'75':
            class_two+=1
    print ('2+|','X'*class_two,sep='')
    
    class_three=0
    for i in history:
        if '60'<=i<'70':
            class_three+=1
    print ('2-|','X'*class_three,sep='')
    
    class_four=0
    for i in history:
        if '50'<=i<'60':
            class_four+=1
    print ('3 |','X'*class_four,sep='')
    
    class_five=0
    for i in history:
        if i<'50' and i != '100':
            class_five+=1
    print ('F |','X'*class_five,sep='')                
histogram()