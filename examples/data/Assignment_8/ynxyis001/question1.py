#Palindrom or not?
#Jennifer Yuan 
#7 May 2014

s = input("Enter a string: \n") #gets input from user

def palin(x,s):
    if len(s)%2 ==0: #if length of string is even
        if x==len(s)//2: #stops recursion at the middle of the string, as then all letters have been checked
            print("Palindrome!")
        else:
            if s[x] == s[-(x+1)]: #checks to see if first and last letter are the same
                palin(x+1, s) #if the first and the last are the same, then it continue to check the if the sencond and second last letter are the same and so one
            else:
                print("Not a palindrome!") #if any "pairs" of letters are not the same, the string is not a palindrome
    else:
        if x==(len(s)//2)+1: #does the same as above, but for an odd lengthed string
            print("Palindrome!")
        else:
            if s[x] == s[-(x+1)]:
                palin(x+1, s)
            else:
                print("Not a palindrome!")        
            
palin(0,s)   #calls functions       
            
                       
            