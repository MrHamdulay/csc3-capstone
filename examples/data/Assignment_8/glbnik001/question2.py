# 9 May 2014
# Checks to see how many pairs occur in a string
# Nikhil Gilbert

lis = [] #stores the number of pairs
# This function keeps track of the number of pairs that occur and is called in the function "pair"
def tracker(x):
    if x == 1:
        lis.append(1)

#This is the actual function that involves the recursive step        
def pair(n):
    if len(n)<2:
        return False
    if n[len(n)-len(n)] == n[len(n)-len(n)+1]:
        tracker(1) #counter function called 
        return pair(n[2:])
    if len(n) > 2:
        return pair(n[1:]) #shortens the length of the string by the letter already checked 
#Main programme that prompts user and prints pairs
def main():
    n = input ("Enter a message:\n")
    pair(n)
    print ("Number of pairs:", len(lis)) 

main()
    
        