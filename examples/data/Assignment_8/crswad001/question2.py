'''Wade Cresswell
Question 2'''
string = input("Enter a message:\n")
def numpair(stringused):
    z = len(stringused)
    if z == 1:
        return 0 #if string gets to the point where the length is 1, dont add anything to the pair counter
    if z!=1 and z!=2: #if the string is currently not 1 or 2 letters long
        if stringused[0]==stringused[1]:
            stringused=stringused[2:]
            return 1 + numpair(stringused) #if the two alternate characters are equal, return the rest of the string
        else:
            return numpair(stringused[1:]) #otherwise return the rest of the string
    else:
        if stringused[0]==stringused[1]:
            return 1
        else:
            return 0
print('Number of pairs:',numpair(string)) #prints the number of pairs in the string

