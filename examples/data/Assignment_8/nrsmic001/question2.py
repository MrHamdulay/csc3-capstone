"""program to count a number of pairs of repeated characters
Micaela Narasmulu
09 May 2014"""

count=0 #initialise count to be 0

def county(string):
    global count
    if string=='':
        return count
    
    else:
        
        if(len(string)>1 and string[0]==string[1]):
    
            count=count+1
        
            return county(string[2:len(string)])
        else:
            return county(string[1:len(string)])

m=input("Enter a message:\n")        #get input from user

print("Number of pairs:",county(m))
