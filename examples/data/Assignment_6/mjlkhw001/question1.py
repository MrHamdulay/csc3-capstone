# Right Align Program
# Khwezi Majola
# MJLKHW001
# 19 April 2014

def right():
    imax = 0 #The max string length
    names = [] #The list in which the input will be placed
    string = input('Enter strings (end with DONE):\n') #Initial string input
    while string != 'DONE': #Continues to ask for input until DONE is entered
        names.append(string)
        string = input()
    for i in range(len(names)): #Find the max string length
        imax = max(imax, len(names[i]))
    print('\nRight-aligned list:') 
    for i in range(len(names)):
        output = ('{0:>' + str(imax) +'}').format(names[i]) #Format the string
        print(output) #Print the string
right() 