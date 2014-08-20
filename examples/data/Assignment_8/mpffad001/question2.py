"""a program that uses a recursive function to count the number of pairs of repeated characters in a string
fadzai mupfunya
08 may 2014"""

message = input("Enter a message:\n")

#to split the sentence into individual characters
#message2=list(message)

def count_characters(s, count):
    
    #base case to check whether the length of the word is greater than 1
    if len(s)<2:
        print("Number of pairs:", count)
        return
    #to check if the first character in list is the same as the second character and add store the number of pairs in a count variable
    elif s[0] == s[1]:
        count+=1
        return count_characters (s[2:], count)
    #if characters are not equal then it should remove the first character 
    else:
        return count_characters (s[1:], count)
    print("Number of pairs:", count) 
    
count_characters(message,0)
   