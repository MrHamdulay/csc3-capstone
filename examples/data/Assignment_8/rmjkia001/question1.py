"""Check if a string is a palindrome
Kiara Ramjith
May 2014"""
def pal(s,test):
    if(len(s)!=0): #if the lengths are not =
        test=test+ s[len(s)-1]#adds the last char to the test
        return pal(s[0:len(s)-1],test)# function with the next letter d=from the back
    else: 
        return(test) #returns the string backwards
if __name__=="__main__":
    s=input("Enter a string:\n")
    t=pal(s,"") #calls the function that reverses the string
    if(t==s): #if they are equal backwards and wards; come in
        print("Palindrome!")
    else:
        print("Not a palindrome!")
