#dean makambwa
#6/05/14
#program to check the number of pairs of repeated characters

#get input from user 
n=input('Enter a message:\n')

def pairs(n):
    #check if input is empty or if its a single character and return 0
    if n=='':
        return 0 
    elif(len(n)==1):
        return 0 
    #otherwise if the first letter is the same as the second one then return 1+the addition number if pairs othewrise if its the consecutive characters are not the same then remove the first one then continue checking the rest of the string 
    else:
        if n[0]==n[1]:
            n=n[2:]
            return 1 + pairs(n)
        else:
            return pairs(n[1:])
#create a variable of the function then use it to print the string of whatever it returns
x=pairs(n)
print('Number of pairs: '+str(x))