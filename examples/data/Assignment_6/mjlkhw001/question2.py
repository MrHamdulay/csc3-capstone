# Vector calculations
# Khwezi Majola
# MJLKHW001
# 19 April 2014

def vectorcalc():
    import math #Import the math module for later use
    svecA = input('Enter vector A:\n') #Take in vector A values as a string
    svecB = input('Enter vector B:\n') #Take in vector B values as a string
    vecA = svecA.split() #Create a list from the string
    vecB = svecB.split() #Create a list from the string
    add = ['']*3 #Empty list for addition
    for i in range(3):
        add[i] = eval(vecA[i] + '+' + vecB[i])
    multi = 0 #Create integer for multiplication
    for i in range(3):
        multi += eval(vecA[i] + '*' + vecB[i])
    sqrtA = 0.0 #Create float for absolute value
    sqrtB = 0.0 #Create float for absolute value
    tempA = 0 #Temporary integer for use
    tempB = 0 #Temporary integer for use
    for i in range(3): #Summing the squares
        tempA += eval('('+vecA[i]+')'+'**2') 
        tempB += eval('('+vecB[i]+')'+'**2')
    sqrtA = math.sqrt(tempA)
    sqrtB = math.sqrt(tempB)
    print('A+B =',add)#Displaying the values
    print('A.B = ' + str(multi))
    outsq = '|A| = {0:.2f}'.format(sqrtA)
    print(outsq)
    outsq = '|B| = {0:.2f}'.format(sqrtB)
    print(outsq)
vectorcalc()