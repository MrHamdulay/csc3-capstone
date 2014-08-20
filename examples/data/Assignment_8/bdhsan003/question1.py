#Sandisha Budhal
#09 May 2014



def rvs(wrd):# function to reverse a string
    if len(wrd) == 0 or len(wrd) == 1:
        return(wrd)
    else:
        return wrd[len(wrd) - 1] + rvs(wrd[1:len(wrd) - 1]) + wrd[0]
    

def palindrome():
    wrd = input("Enter a string:\n")
    
    if rvs(wrd) == wrd:   #the input supplied from user is compared to reversed string
        print("Palindrome!")
    else:
        print("Not a palindrome!")
palindrome()