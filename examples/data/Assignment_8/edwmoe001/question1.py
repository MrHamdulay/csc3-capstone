""" Program for recursive palindrome
Tauhirah Eguardo
2014/04/05"""
    
def main():
    word = input("Enter a string:\n")
    amount = len(word)
    start = 0
    newword =""
    revword = swapper(word,start,newword)
    
    if revword == word:
        print("Palindrome!")
    else:   
        print("Not a palindrome!")
            
            
def swapper(msg,start,revword):
    if msg == "":
        return revword
        
    else:
        revword += msg[-1] 
        msg = msg[:-1]
        return swapper(msg,start,revword)
    


main()