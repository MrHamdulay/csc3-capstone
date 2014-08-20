'''Program using recursion to count the number of paired characters in message
nkosi gumede
7 may 2014'''

listed=[]
def paired_strings(message):
    if len(message)<=1:
        #This is your quit condition
        print("Number of pairs:",len(listed))
    else:
        #If length of message is 2 or more
        if message[0]!=message[1]:
            #Not going to count anything
            paired_strings(message[1:])
        if message[0]==message[1]:
            #1 count must be added
            listed.append(1)
            paired_strings(message[2:])


if __name__=='__main__':
    x=input("Enter a message:\n")
    paired_strings(x)