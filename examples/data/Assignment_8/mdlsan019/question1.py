'''Check to see if a string is palindromic
   Sanele Mdlalose
   07 May 2014'''


s=input("Enter a string:\n")
l_str=len(s)//2
str_r = s[l_str+1:]
def palindrome(s):
    global str_f
    if s=='' :
        return s
        
    else:
        
        s_new=s[:l_str+1]
        str_f = palindrome(s[1:l_str]) + s[0] 
        return str_f

ans1="Palindrome!"
ans2="Not a palindrome!"            
x=palindrome(s)
if len(s)%2==0:
    str_r=s[l_str:]
    if str_f == str_r:
        
        print (ans1)
    else:
        print (ans2)
else:
    
    if str_f == str_r:
            
        print (ans1)
    else:
        print (ans2)    
            
                   