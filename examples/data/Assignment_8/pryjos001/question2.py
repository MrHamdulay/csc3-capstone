"""Program using recursion to find number of character pairs in string
Joseph Preyer
6 May 2014"""

message = input("Enter a message:\n")

def pairs(message,count):
      
    #Base case: no output if message is empty
    if len(message)>1:
        #If a pair is found in first 2 characters, add 1 to count and call function with message[2:]
        if message[0]==message[1]:
            pairs(message[2:],count+1)
        #If first character not equal to second character, call function with message[1:]
        elif message[0]!=message[1]:
            pairs(message[1:],count)
    #When the string is too short to have any more pairs, print count
    else:
        print ("Number of pairs:", count)
pairs(message,0)