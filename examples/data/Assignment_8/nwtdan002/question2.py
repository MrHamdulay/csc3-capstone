'''A Program to find the number of pairs of equal characters within a string
By Daniel Newton
04/05/14'''

def findpairs(string,count):
    if len(string)<2:   #All possibilities of pairs have been checked for, therefore final count must be returned
        return count
    if string[0]==string[1]:    #Checks for pair in first 2 characters. If found, returns the function to exclude those characters and check the next two.
        count+=1
        return findpairs(string[2:],count)
    else:   #If no pair found, returns function excluding the first character to check again for a pair.
        return findpairs(string[1:],count)

count=0
string=input("Enter a message:\n")  #prompts user input of a string, and runs the function to check for number of pairs.
print("Number of pairs:",findpairs(string,count))