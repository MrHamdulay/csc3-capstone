"""program that uses a recursive function to count the number of pairs of repeated characters in a string
vuyolwethu nkosi
4 may 2014"""

msg=input("Enter a message:\n") #get message from user
def count_the_pairs(msg):
    #message=input("Enter a message:\n")
    if len(msg)<=1: #if the string is empty or if it only has one letter ie.Base case
        return 0
    elif msg[0]==msg[1]: #if the letter is the same as the letter next to it
        return 1 + count_the_pairs(msg[2:]) #return 1 and add the call of the next function ie.Recursive step
    else:
        return count_the_pairs(msg[1:]) #if there's no pairs it should return none
print("Number of pairs:",count_the_pairs(msg)) #print the output
                         #calling the function
    