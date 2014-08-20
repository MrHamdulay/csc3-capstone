'''Q2 of Assignment 8: Counting number of pairs of repeated characters in a string
Patrick Boroughs
4 May 2014'''

def pairs(string,count):
    
    #base case. whole string tested
    if len(string)<=1:
        return count
    
    #adjacent characters match, return string after pair and add to pairs count
    elif string[0]==string[1]:
        return pairs(string[2:],count+1)
    
    #no match, send in string 1 character smaller
    else:
        return pairs(string[1:],count)

#input and printing    
print("Number of pairs:",pairs(input("Enter a message:\n"),0))