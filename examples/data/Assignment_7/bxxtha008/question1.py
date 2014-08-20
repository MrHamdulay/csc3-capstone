'''progam to print out strings
Thabiso Beau
28 April 2014
Assignment 7: #question1.py'''

#the question is basically like the one in the previous assignement in structure


def main():
    strings=input('Enter strings (end with DONE):\n') #assignment statement for the strings to be entered
    X=[] #empty list to which we append the list
    while strings!='DONE': #sentinel loop
        X.append(strings) #append strings to empty list 
        strings=input('')
#part 2 for printing list without duplicates 
    Y=[] #create an empty list for appending of strings
    print()
    print('Unique list:')
    for i in X: #counting no. of occurrences in a list for it to be printed
        if i not in Y: #we test if the word features in the list or not
            Y.append(i) #if not, append the word to list
            print(i)
        #REMEMBER THAT AN IF STATEMENT CAN STAND ALONE, BUT ELSE CAN'T 
main()