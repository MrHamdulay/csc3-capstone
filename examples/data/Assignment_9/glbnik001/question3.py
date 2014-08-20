# May 16 2014
# Nikhil Gilbert
# Check Sudoku grid

#each of the following conditions ensure that validity is always kept true
happy = True 
happy2= True
happy3= True
happy4= True
happy5= True
checker = []
#online, taken from stackoverflow
collector =[]
for i in range(9):
    collector.append([]*9)
for i in range(9):
    line = str(input())
    Input = list(line)
    for k in range(9):
        collector[i].append(Input[k])

#Checks to see if rows match
for c in range(len(collector)):
    #appends a to a list and checks for consistency
    for a in collector[c]: 
        checker.append(int(a))
    checkercount = 0
    for a in checker:
        checkercount = checkercount+a
    
    if checkercount == 45:
        happy = True
    else:
        happy = False
    
    checker = []
    checkercount = 0

colchecker = [] #new list for new part

#checks to see if columns match
for num in range(9):
    for b in collector:
        colchecker.append(b[num])
    colcount=0
    for d_0 in colchecker:
        colcount = colcount + int(d_0)
    
    if colcount == 45:
        happy2 = True
    else:
        happy2 = False
    
    colchecker = []
    colcount = 0

subg=[]
subgridcount=0
#check subgrids
for n in range(3):
    #appends a to a list and checks for consistency
    for m in collector[n][:3]: 
        subg.append(int(m))
    for m in subg:
        subgridcount = subgridcount+m
    
    if subgridcount == 45:
        happy3 = True
    else:
        happy3 = False
    
    subg = []

subgridcount = 0
for n in range(3,6):
    #appends a to a list and checks for consistency
    for m in collector[n][:3]: 
        subg.append(int(m))
    for m in subg:
        subgridcount = subgridcount+m
    
    if subgridcount == 45:
        happy4 = True
    else:
        happy4 = False
    
    subg = []

subgridcount = 0
for n in range(6,9):
    #appends a to a list and checks for consistency
    for m in collector[n][:3]: 
        subg.append(int(m))
    for m in subg:
        subgridcount = subgridcount+m
    if subgridcount == 45:
        happy5 = True
    else:
        happy5 = False
    subg = []

if happy == True and happy2 == True and happy3 == True and happy4 == True and happy5 ==True:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        
