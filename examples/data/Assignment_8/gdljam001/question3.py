"""James Godlonton
recursive encryption
04 May 2014"""


def main():
    """main function for all input and output"""
    print ("Enter a message:")
    message=input("")
    print("Encrypted message:\n"+encrypt(message,0,1))
    
    
    
def encrypt(message,letter,cc):
    """recursive encryption goes through each letter changing it (according to caesar cypher cc) and adding to string """
    #Note: in this case the caesor cypher will always be one but for re usability it is made a variable, to that
    #its easy to change for something more complex e.g. Engima code
    if letter==len(message):
        #Return blank string once you reach the end
        return ""
    elif 96<ord(message[letter])<123:
        #if its lower case add the letter (encrypted) to new message and call recursion again
        if (ord(message[letter])+cc)<123:
            newMess=str(chr(ord(message[letter])+cc))+encrypt(message,letter+1,cc)
        else:
            newMess=str(chr(ord(message[letter])+cc-26))+encrypt(message,letter+1,cc)
    else:
        #if its not lower case...dont encrypt
        newMess=message[letter]+encrypt(message,letter+1,cc)
    #return the new message at the end    
    return newMess




if __name__=="__main__":
    main()
