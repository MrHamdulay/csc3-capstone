'''program to check completion of sudoku puzzle
Thabiso Beau
Assignment 9: #question3.py'''


#Sudoku.py
correct = True #when statemens are correct it will deliver this
guard = []
#part 1 of creating exterior part of the list
list_1 = []
for i in range(9):
    list_1.append([]*9) #create empty 2-d list
    
for i in range(9):
#assign variable to which str function will act on input of empty string or something like that
    lines = str(input())
    X = list(line)
    for j in range(9):
        list_1[i].append(X[j])
print(list_1)

#possible matching of rows is checked by Python

for a in range(len(list_1)):
    #consistency is checked - adds b to list
    
    for b in list_1[a]:
        guard.append(int(b))
    count = 0
    
    #don't know what to do from here on - ask tutor!