''' Program to find palindromes with recursion
Luke Naude
7 May 2014'''

string=input('Enter a string:\n')
start=0
end=len(string)-1
palindrome=1 #start assuming it is a palindrome

def get_string(string):
    global palindrome
    global end
    global start #pull the beginning variales into the function
    if string[start]==string[end] and (start==end or start+1==end): #check that the middle or middle two letter/s fit the palindromic parameters
        return True 
    elif string[start] == string[end]: #compare outer corresponding letters
        start+=1
        end-=1 #check subsequent inner letters
        get_string(string) #repeat
        return True
    if string[start] != string[end]:
        palindrome=0  #palindrome is false if it doesnt fit once      
        return False
    
    


    
    

    
get_string(string)
if palindrome==0:
        print('Not a palindrome!')
if palindrome==1:
        print('Palindrome!')  
    
 
    



   