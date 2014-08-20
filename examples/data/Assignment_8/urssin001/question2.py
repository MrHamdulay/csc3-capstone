#Write a program that uses a recursive function to count the number of pairs
#of repeated characters in a string. Pairs of characters cannot overlap. 
#Sinead Urisohn
#6 May 2014

#get message
message=input("Enter a message:\n")
#create recursive function to count number of pairs that receives message as parameter
def count_pairs(m):
    #base case if string empty or only has one character left
    if m=="" or len(m)==1:
        return 0
    #compare consecutive characters to check for pairs
    #if pair found
    elif m[0]==m[1]:
        #increase number of pairs by 1 and repeat recursive step 
        return 1+count_pairs(m[2:])
    #else no pair found
    else:
        #repeat recursive step by slicing off first two characters and sending in rest of string
        return count_pairs(m[2:])
#display results
print("Number of pairs:",count_pairs(message))