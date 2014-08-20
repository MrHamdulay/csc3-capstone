"""program to determine wether a string is a palindrome or not
author: DIVAN JAGERS
date : 9 May 2014"""
def palindrome(item=input("Enter a string:\n")):
    if item == "":
        return True   #base case
    if len(item)<=1:
        return True    #base case
    else:
        if item[0] == item[len(item)-1]:   #checks if first character is equal to the last character 
            item = item[1:-1]       #it now slices the item
            if palindrome(item):     #if it is a palindrome then it will print "Palindrome!"
                print("Palindrome!")
        else:        #otherwise it prints that it is not a palindrome
            print("Not a palindrome!")
palindrome()