#palindrome through recursion
#michael field
#4 april 2014

def palin(string, count):
    
    if count == len(string):
        print("Palindrome!")
    
    elif string[count] == string[len(string)-count-1]:
        count += 1
        palin(string, count)
        
    else:
        print("Not a palindrome!")
    
string = input("Enter a string:\n")
count = 0

palin(string, count)