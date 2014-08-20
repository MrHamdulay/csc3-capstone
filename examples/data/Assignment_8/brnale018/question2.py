# Alex Brunette
# 07/05/2014
# Program to count number of pairs of repeated characters in a string
def main():    
    string = input("Enter a message:\n") #get string
    y = double_char(string)
    print("Number of pairs:" , y)

def double_char(string):
    if string=='': #if nothing entered
        return 0
    if len(string) == 1: #string cannot have pairs if the length is 1
        return 0
    if string[0] != string[1]: #if the first character is not the same as the second, remove first character and do recursive step 
        return double_char(string[1:])
    if string[0] == string[1]: #if there are pairs, add 1 to a count
            count = double_char(string[1:])
            count = count + 1
            return count
    if string[0] == string[1] and string[0] == string[2]: #if 3 consequtive characters are the same, delete the third character
        string=list(string)
        del(string[2])
        return double_char(string[1:])


main()    
        