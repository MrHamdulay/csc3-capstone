#Count the Number of pairs
# Michael Sanne
# 2014/05/05

#Checks to see if there is a pair
def checker (String, position):
    if (String[position] == String[position+1]):
        return 1
    else:
        return 0
#runs through the String and sends new characters into the checker and sums up the total
def pairs (String, position):
    counter = 0
    if (position >= len(String)-1):
        return counter
    else:
        if (checker(String, position) == 1):
            #if there is a pair +2 because the program must skip the entire pair
            return counter + 1 + pairs(String, position+2)
        else:
            return counter + pairs(String, position+1)
    
#Asks the user for input
String = input ("Enter a message:\n")
number = pairs(String, 0)
#Outputs the sum
print("Number of pairs: " + str(number))