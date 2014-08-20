'''program takes a list of marks and outputs a histogram representation
sankara mallane
23 april 2014'''

# empty list
listMarks = [] 

# create a dictionary
markCategories = {'1 ':0, '2+':0, '2-':0, '3 ':0, 'F ':0}

# get a list of marks from user
marks = input("Enter a space-separated list of marks:\n")

# separate into list of marks
listMarks = marks.split (" ")

# convert string in list to numbers
for i in range (len(listMarks)):
    listMarks[i] = eval(listMarks[i])
    
    # check marks and increase to the right categories
    if listMarks[i] >= 75:
        markCategories['1 '] += 1
    elif listMarks[i] >= 70:
        markCategories['2+'] += 1
    elif listMarks[i] >= 60:
        markCategories['2-'] += 1
    elif listMarks[i] >= 50:
        markCategories['3 '] += 1
    else:
        markCategories['F '] += 1        
        
# print out the horizontal bars in order of highest category to lowest        
for key in sorted( markCategories.keys()):
    horizontalBar = 'X'*markCategories[key]
    print(key, '|', horizontalBar, sep='')
