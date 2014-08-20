'''Program that prints out a list of strings which have been right-aligned; program terminates when 'DONE' is entered.
HAMZA EBRAHIM
25/04/14.''' 

# Assignment 6 - Question 1


# initialise empty list

strings = [] 

# prompt user for input

x = input("Enter strings (end with DONE):\n") 


# state condition which terminates sentinel (while) loop; also appends user input to the list created and creates condition for correct alignment

while x != 'DONE':
    strings.append(x) 
    x = input('') 
    
    z = 0 
    for i in strings:
        if len(i) > z:
            z = len(i)

# prints out list of strings which are right aligned   

print("\nRight-aligned list:")
for string in strings:
    print(' '*(z-len(string)), string, sep='')

       
# program ends
