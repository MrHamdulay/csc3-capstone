# question1.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 07 May 2014

def palin(string):
    if len(str(string))<2:
        return True                                                             #if length of string is < 2, then we have a palindrome, thus return True
    elif (palin(str(string)[1:-1]) and str(string)[0] == str(string)[-1]):      #checks if first == last character of string and slices those characters from the string
        return True                                                             #returns True if above condition is met
    else:
        return False                                                            #returns False if string is not a palindrome
        
if __name__ == '__main__':
    string = input("Enter a string:\n")                                         #get input (string) from user
    palin(string)                                                               #run function palin(string) to check if string entered is a palindrome
    if palin(string):
        print("Palindrome!")                                                    #prints "Palindrome!" if string entered is a palindrome
    else:
        print("Not a palindrome!")                                              #prints "Not a palindrome!" if string entered is not a palindrome