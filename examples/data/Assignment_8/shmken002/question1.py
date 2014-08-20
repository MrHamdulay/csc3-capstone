"""checking to see whether string is palindromic
ringo shima
6/5/14"""
#get sentence



def pal(str0):
    
    """if str != "": #if there's something 
        #print(str0[len(str0)//2]) #test half way point"""
    
    if str0 == "": #base case/no string
        return "Palindrome!"
    
    elif str0[0] == str0[len(str0)-1]: #compare 1st and last chrs
        return pal(str0[1:-1]) #get slice of string without 1st/last chrs
    
    else:
        return "Not a palindrome!"
        
if __name__ == "__main__":
    str0 = input("Enter a string:\n") 
    print(pal(str0)) 
    