"""Program to count pairs of characters in a string
thushar hariparsad
7 May 2014"""


string = input("Enter a message:\n")

#create a counter to keep track of the number of pairs of characters
count = 0

def count_pairs(string):
    global count
    if len(string) <= 1:
        print("Number of pairs:", count)
    
    #If the first 2 characters in the string are the same, delete both and add 1 to the counter.        
    elif string[0] == string[1]:
        count += 1
        string = string[2:]
        return count_pairs(string)
    
    #If the first 2 characters in the string are not the same, delete only the first one    
    else:
        string = string[1:]
        return count_pairs(string)
    
if __name__=="__main__":
    count_pairs(string)
    
                            