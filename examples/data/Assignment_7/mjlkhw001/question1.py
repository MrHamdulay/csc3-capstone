# Print words without duplicates
# Khwezi Majola
# MJLKHW001
# 27 April 2014

def dup():
    Word_In = input('Enter strings (end with DONE):\n') #Intial input
    Word_Li = [] #Empty grid
    while Word_In != 'DONE': #Ensure continous input until DONE is entered
        if Word_In not in Word_Li: #Checks if the words is in the list
            Word_Li.append(Word_In)
        Word_In = input()
    print('\nUnique list:')
    for a in Word_Li: #Prints the unique words
        print(a)
dup()