""" Question 2 / Assignment 8: Count pairs of repeated strings
Shaheel Kooverjee - KVRSHA004
8 May 2014 """

def countpairs(string):
    if len(string) == 1: #base case
        return 0
    else: 
        if string[0] == string[1]: #if first character identical to second
            if len(string) > 2:
                if string[1] == string[2]: #if second character identical to third:
                    return 1 + countpairs(string[2:]) #repeat function with string minus first two identical characters - add 1 to count
                else:
                    return 1 + countpairs(string[1:]) #else repeat function with string minus first character - add 1 to count
            else:
                return 1 + countpairs(string[0]) #if string only two characters long and characters identical - add 1 to count
        else:
            return countpairs(string[1:]) #if first character not identical to second, repeat funtion with string minus first character
    
userstring = input("Enter a message:\n")
print("Number of pairs:", countpairs(userstring))