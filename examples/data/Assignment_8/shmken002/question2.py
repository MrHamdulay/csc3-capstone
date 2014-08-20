"""checking for number of pairs in message
ringo shima
7/5/14"""


def pairs(mssg, counter):
    
    #x = str(mssg)
        
    if mssg == "": #base case-no pairs
        return counter
    elif len(mssg) == 1: #base case- no pairs but 1 letter
        return counter
    elif mssg[0]==mssg[1]: #start at 1st and 2nd letters
        counter +=1      
        return pairs(mssg[2:],counter) #start after the pair til end
    else:
        return pairs(mssg[1:],counter) #start at the number after the single (non paired) number

def main():
    mssg = input("Enter a message:\n") 
    print("Number of pairs:", pairs(mssg,0)) #here's where you call the function and assign counter's starting value
main()
